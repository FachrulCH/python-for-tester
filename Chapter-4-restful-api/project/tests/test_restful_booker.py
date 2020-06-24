import requests
from assertpy import assert_that
import restful_booker
import json


def print_request(request: requests):
    print('\n-----------Request----------->')
    print(request.method, request.url)
    headers = '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items())
    print(headers)
    print(request.body)


def print_response(response: requests.Response):
    data = response.json()
    body = json.dumps(data, indent=4)
    resp_body = body
    print('\n<-----------Response-----------')
    headers = '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items())
    print(headers)
    print(resp_body)


class TestRestfulBooking():
    def test_get_list_of_all_booking(self):
        resp = restful_booker.get_bookings()
        print_request(resp.request)
        print_response(resp)
        assert_that(resp.status_code, 200).is_true()
        assert_that(len(resp.json())).is_greater_than(0)

    def test_get_booking_detail(self):
        resp = restful_booker.get_detail_booking(6)
        print_request(resp.request)
        print_response(resp)
        assert_that(resp.status_code, 200).is_true()
        assert_that(resp.json().get('firstname')).is_not_empty()

    def test_create_booking(self):
        resp = restful_booker.create_dummy_booking()
        print_request(resp.request)
        print_response(resp)
        created_booking = resp.json()
        print('bookingid = ', created_booking['bookingid'])

    def test_booking_flow(self):
        # Given I have booking data
        booking_data = restful_booker.generate_dummy()
        print('booking_data: ', booking_data)
        # When I create booking
        create = restful_booker.create_booking(booking_data)
        assert_that(create.status_code, 200).is_true()
        # Then I should see booking created correctly
        booking_id = create.json().get('bookingid')
        print('booking_id: ', booking_id)
        get_booking = restful_booker.get_detail_booking(booking_id)
        booking_detail = get_booking.json()
        assert_that(get_booking.status_code, 200).is_true()
        assert_that(booking_detail['firstname']).is_equal_to(booking_data['firstname'])
        assert_that(booking_detail['lastname']).is_equal_to(booking_data['lastname'])
        assert_that(booking_detail['bookingdates']['checkin']).is_equal_to(booking_data['bookingdates']['checkin'])

    def test_update_booking(self):
        auth_token = restful_booker.get_authtoken()
        
