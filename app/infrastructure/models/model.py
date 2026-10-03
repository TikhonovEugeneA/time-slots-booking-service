from sqlalchemy import String, Boolean, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import CITEXT

from uuid import UUID
from datetime import datetime


from app.domain.users import User, UserRole
from app.domain.time_slots import TimeSlot, TimeSlotStatus
from app.domain.bookings import BookingStatus
from app.domain.specialists import Specialist
from app.domain.bookings import Booking
from app.domain.audit_logs import AuditLog
from app.domain.service_centers import ServiceCenter


from app.infrastructure.models import Base, CreatedAtMixin, MetadataMixin


class UserModel(Base, CreatedAtMixin):

    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(CITEXT(320), unique=True)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    specialist: Mapped["SpecialistModel"] = relationship(
        "SpecialistModel", back_populates="user", uselist=False
    )

    bookings: Mapped[list["BookingModel"]] = relationship(
        "BookingModel",
        back_populates="client",
    )

    audit_logs: Mapped[list["AuditLogModel"]] = relationship(
        "AuditLogModel",
        back_populates="actor",
    )

    def to_domain(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            role=self.role,
            is_active=self.is_active,
            created_at=self.created_at,
        )

    @classmethod
    def from_domain(cls, user: User) -> "UserModel":
        return cls(
            id=user.id,
            name=user.name,
            email=user.email,
            role=user.role,
            is_active=user.is_active,
            created_at=user.created_at,
        )


class ServiceCenterModel(Base, CreatedAtMixin):

    __tablename__ = "service_centers"

    name: Mapped[str] = mapped_column(String(200), unique=True)
    address: Mapped[str] = mapped_column(String(500))
    timezone: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    specialists: Mapped[list["SpecialistModel"]] = relationship(
        "SpecialistModel", back_populates="service_center"
    )

    def to_domain(self) -> ServiceCenter:
        return ServiceCenter(
            id=self.id,
            name=self.name,
            address=self.address,
            timezone=self.timezone,
            is_active=self.is_active,
            created_at=self.created_at,
        )

    @classmethod
    def from_domain(cls, service_center: ServiceCenter) -> "ServiceCenterModel":
        return cls(
            id=service_center.id,
            name=service_center.name,
            address=service_center.address,
            timezone=service_center.timezone,
            is_active=service_center.is_active,
            created_at=service_center.created_at,
        )


class SpecialistModel(Base, CreatedAtMixin):

    __tablename__ = "specialists"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    center_id: Mapped[UUID] = mapped_column(ForeignKey("service_centers.id"))
    specialization: Mapped[str] = mapped_column(String(200))
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)

    user: Mapped["UserModel"] = relationship(
        "UserModel",
        back_populates="specialist",
        uselist=False,
        lazy="joined",
    )

    service_center: Mapped["ServiceCenterModel"] = relationship(
        "ServiceCenterModel", back_populates="specialists"
    )

    time_slots: Mapped[list["TimeSlotModel"]] = relationship(
        "TimeSlotModel",
        back_populates="specialist",
    )

    def to_domain(self) -> Specialist:
        return Specialist(
            id=self.id,
            user_id=self.user_id,
            center_id=self.center_id,
            specialization=self.specialization,
            is_available=self.is_available,
            created_at=self.created_at,
        )

    @classmethod
    def from_domain(cls, specialist: Specialist) -> "SpecialistModel":
        return cls(
            id=specialist.id,
            user_id=specialist.user_id,
            center_id=specialist.center_id,
            specialization=specialist.specialization,
            is_available=specialist.is_available,
            created_at=specialist.created_at,
        )


class TimeSlotModel(Base, CreatedAtMixin):

    __tablename__ = "time_slots"

    specialist_id: Mapped[UUID] = mapped_column(ForeignKey("specialists.id"))
    starts_at: Mapped[datetime]
    ends_at: Mapped[datetime]
    status: Mapped[TimeSlotStatus] = mapped_column(
        Enum(TimeSlotStatus), default=TimeSlotStatus.AVAILABLE
    )

    specialist: Mapped["SpecialistModel"] = relationship(
        "SpecialistModel",
        back_populates="time_slots",
    )

    booking: Mapped["BookingModel"] = relationship(
        "BookingModel",
        back_populates="time_slot",
    )

    def to_domain(self) -> TimeSlot:
        return TimeSlot(
            id=self.id,
            specialist_id=self.specialist_id,
            starts_at=self.starts_at,
            ends_at=self.ends_at,
            status=self.status,
            created_at=self.created_at,
        )

    @classmethod
    def from_domain(cls, time_slot: TimeSlot) -> "TimeSlotModel":
        return cls(
            id=time_slot.id,
            specialist_id=time_slot.specialist_id,
            starts_at=time_slot.starts_at,
            ends_at=time_slot.ends_at,
            status=time_slot.status,
            created_at=time_slot.created_at,
        )


class BookingModel(Base, CreatedAtMixin):

    __tablename__ = "bookings"

    slot_id: Mapped[UUID] = mapped_column(ForeignKey("time_slots.id"))
    client_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    subject: Mapped[str] = mapped_column(String(500))
    status: Mapped[BookingStatus] = mapped_column(Enum(BookingStatus))

    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
    cancelled_at: Mapped[datetime | None]
    completed_at: Mapped[datetime | None]

    time_slot: Mapped["TimeSlotModel"] = relationship(
        "TimeSlotModel",
        back_populates="booking",
    )

    client: Mapped["UserModel"] = relationship(
        "UserModel",
        back_populates="bookings",
    )

    audit_logs: Mapped[list["AuditLogModel"]] = relationship(
        "AuditLogModel",
        back_populates="booking",
    )

    def to_domain(self) -> Booking:
        return Booking(
            id=self.id,
            slot_id=self.slot_id,
            client_id=self.client_id,
            subject=self.subject,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at,
            cancelled_at=self.cancelled_at,
            completed_at=self.completed_at,
        )

    @classmethod
    def from_domain(cls, booking: Booking) -> "BookingModel":
        return cls(
            id=booking.id,
            slot_id=booking.slot_id,
            client_id=booking.client_id,
            subject=booking.subject,
            status=booking.status,
            created_at=booking.created_at,
            updated_at=booking.updated_at,
            cancelled_at=booking.cancelled_at,
            completed_at=booking.completed_at,
        )


class AuditLogModel(Base, CreatedAtMixin, MetadataMixin):

    __tablename__ = "audit_logs"

    booking_id: Mapped[UUID] = mapped_column(
        ForeignKey("bookings.id", ondelete="RESTRICT")
    )
    action: Mapped[BookingStatus] = mapped_column(Enum(BookingStatus))
    actor_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))

    booking: Mapped["BookingModel"] = relationship(
        "BookingModel",
        back_populates="audit_logs",
    )

    actor: Mapped["UserModel"] = relationship(
        "UserModel",
        back_populates="audit_logs",
    )

    def to_domain(self) -> AuditLog:
        return AuditLog(
            id=self.id,
            booking_id=self.booking_id,
            action=self.action,
            actor_id=self.actor_id,
            metadata=self.meta,
            created_at=self.created_at,
        )

    @classmethod
    def from_domain(cls, audit_log: AuditLog) -> "AuditLogModel":
        return cls(
            id=audit_log.id,
            booking_id=audit_log.booking_id,
            action=audit_log.action,
            actor_id=audit_log.actor_id,
            meta=audit_log.metadata,
            created_at=audit_log.created_at,
        )
