from fastapi import APIRouter, Request, status, Depends
from fastapi.security import HTTPBearer

from uuid import UUID

from service_router import service_route
from models.booking import BookingCreateForm, BookingUpdateForm
from settings import settings

router = APIRouter(tags=["BOOKING"])
security = HTTPBearer()


@service_route(
    request_method=router.post,
    service_url=settings.BOOKING_SERVICE_URL,
    path="/booking",
    status_code=status.HTTP_200_OK,
    payload_key="booking",
    auth_required=True,
    response_model="models.booking.BookingResponse",
)
async def create_a_booking(booking: BookingCreateForm, request: Request,  # noqa
                           authorization: str = Depends(security)):  # noqa
    """Create a Booking"""
    ...


@service_route(
    request_method=router.get,
    service_url=settings.BOOKING_SERVICE_URL,
    path="/booking",
    status_code=status.HTTP_200_OK,
    payload_key="booking",
    auth_required=True,
    response_model="models.booking.BookingResponse",
)
async def read_all_bookings(request: Request, authorization: str = Depends(security)):  # noqa
    """Read All the Booking Information"""
    ...


@service_route(
    request_method=router.get,
    service_url=settings.BOOKING_SERVICE_URL,
    path="/booking/{booking_id}",
    status_code=status.HTTP_200_OK,
    payload_key="booking",
    auth_required=True,
    response_model="models.booking.BookingResponse",
)
async def read_a_booking(booking_id: UUID, request: Request,  # noqa
                         authorization: str = Depends(security)):  # noqa
    """Read the Specific Booking Information"""
    ...


@service_route(
    request_method=router.get,
    service_url=settings.BOOKING_SERVICE_URL,
    path="/booking/user/{user_id}",
    status_code=status.HTTP_200_OK,
    payload_key="booking",
    auth_required=True,
    response_model="models.booking.BookingResponse",
)
async def read_all_bookings_by_a_user(user_id: UUID, request: Request,  # noqa
                                      authorization: str = Depends(security)):  # noqa
    """Read all Booking Information by a User"""
    ...


@service_route(
    request_method=router.put,
    service_url=settings.BOOKING_SERVICE_URL,
    path="/booking/{booking_id}",
    status_code=status.HTTP_200_OK,
    payload_key="booking",
    auth_required=True,
    response_model="models.booking.BookingResponse",
)
async def update_a_booking(booking_id: UUID, booking: BookingUpdateForm, request: Request,  # noqa
                        authorization: str = Depends(security)):  # noqa
    """Update the Specific Booking Information"""
    ...


@service_route(
    request_method=router.delete,
    service_url=settings.BOOKING_SERVICE_URL,
    path="/booking/{booking_id}",
    status_code=status.HTTP_200_OK,
    payload_key=None,
    auth_required=True,
)
async def delete_a_booking(booking_id: UUID, request: Request, authorization: str = Depends(security)):  # noqa
    """Delete the Specific Booking"""
    ...
