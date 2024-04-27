from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework import status
import requests
from datetime import datetime, timedelta
import json
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.

class get_fight_deatils(APIView):
    renderer_classes = [JSONRenderer]
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self, request):

        data = request.data

        # Validate request data
        required_fields = ['adults_count', 'young_adults_count', 'children_count', 'infants_count',
                           'departure_date', 'origin_location', 'destination_location']
        for field in required_fields:
            if not data.get(field):
                return JsonResponse({'Message': f'{field} field is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = self.swiss_air(**data)
            # print("The resonse of main api is: ",response.text)

            # res= response.json()
            return JsonResponse({'Message': "Success", 'Result': response}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Message': "Failure", "Result": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

    def get_token(self):

        url = "https://api-shop.swiss.com/v1/oauth2/token"

        payload = {
            "client_id": "8reubuqz8gkn2vs3wbenb4zg",
            "client_secret": "FTaj$p54j",
            "fact": '{"keyValuePairs":[{"key":"country","value":"DE"}]}',
            "grant_type": "client_credentials"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://shop.swiss.com",
            "Referer": "https://shop.swiss.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"99\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Akamai-Bm-Telemetry": "a=3635805540034FFCDE6C800F12C8C166&&&e=ODM0MzExRTAxMjYwNERGRTQyREI2OUVGMzQ2MzRDMTZ+WUFBUXp5RVBGL0VEcE0rT0FRQUFoR3BQRkJjOVRncDNMcVdtbXRua2k3QTE5L0tZejh5eHByVjJ3cVltZDlTVWEwQi9UUldaczlsNkVBUCtNUldNZ3pMTXFNMVR5MFJvNEI2VTV3aUJJUm5Gd2tnbW14enFNaFBVdHNxUm9MM3RTWjNPYTQxZ0VHVHlxRFZZYVV1ZTkwTWV5OVN3WnRtcEVZbUxibG5sRXlJMGVtQmxKQzVGVy9DMytFU3k1V21hZERDTlFhbUh4OFpCeXphNjZSNkNncWtlN2hSMEFTamRIVkpFaXlURXAvVzdOcXMrNHJ4dzVZd09IRzRDMk5HeTYxbkE0YjlaOVNIRS94ZEpleURSci9wOVllVTZLZEFPWm5QZTBuZzlLSm94NW1ITHNUdWNJcDExRUJqellLKzVnSHhpR2k1cEV5QlVFMXkxcDVtQ2tKdnJ1cmd5K2FZSWhiNzRHWC9vdFdKNDR2VkhZUFZaZFNnc0NtUjNDYS9NTW5oc3dGaURDa0dVaWJYbThXcGVyZ1RqVUVUSWg1bmp5U0hrdWtOR2VsRT1+MzE2MDM3MX4zNDg2MDIy&&&sensor_data=MjszMTYwMzcxOzM0ODYwMjI7NCwzMiwxLDAsMiw2MjtCMnloTyNxN1pKSnBnMChvcTR7OjsqJW84bmZjLktDbWdQVkYzYSMpW0M/ekNDfi9ZS2BZNHd3VCVfTVQtSHEsMmh3ZmRENFR9PDRsTj5gP1libyorPTM0Z0NBRG1KPTgvfEJNUEhHK2JCIW8vMypGT3J8P0xkZVo3eyQwb3A4MyN+QDVCKXdMdHFkN3FNe01DcXhYYHJ7LFtOT25GK3deYlZGNERyQn5OY3tSNi9fJigtUyxhKik0LGJ5a1hYKHlrcyssVE08fHV8PzFzLjFYeUxmRVdfZWs4bzJdPCgoYFZoZ004RjkodjRUTztPZjRFfkUoRHYsNy59U2UyUHFXSTdbXnwmLll9SV1fTDkqam9KRkJ3NUtmT3xQdGNEXjp+Mk9xQUVtLy55Z2BWcjthX08vOlpFP193eT1dI0ZZbDE1eixDbTZNVHdZVl18JmhbTDNrRltqdyQ2MGluWFQ8e3dTdk5edSF+WT01LXQzJVI1I2tFMll+ITVqTFZJRTlwIWApPylRP1UxdiYpUytyU08le1BFckJMXjssLDJWdVQkYTpyJlNqdFkxJmA5NVoqO29NZWZxUG99YEVgbDZmQ3ZUK24+a3Iqa19+JGdNLnR3cX1UQnZbezl9byNEbD53VE1+ZjE1JEt8bDZKNGppTFlAJk5Xc114N0AwOFkrYUdYKXFJc1pkLCh8OmRFeyN6JSUtIyllRXA8LjROb0l7SVtkJCFkNWEqJSFCYWY3PjZOVFMzRH1waiYhJFhsXT8jTnxvVy94QHZkZjdhXkFPTVtneXoydnA0dnZ3Q3FSPUokJX15UURmSExOLFJZS0tUeE9ERmdNdXhIeztwXTU6dTc+KSxxcl8+VE5aZUs0aGZVQmtmRndrdjxXY1ZORSArJmg4TiB+YDlPWDd2IG85QHB9PVllbXxXMFNYRXZzdXVqLC0vMDNsQWJuWz9MVHV+T3AwTXBxfV1QbiRuP0c4Tlp1IC8oJGNWazR5XnZ3RGEzS35BY2Z9dllROS9kdmsjN1RXdXItVkxxMi1zITpkemIhYCM/W21oWnpKOn0kN0MsLURFVWFMNG44KXhAQnxHJEEvVy8vX1dCeE0pJUUyYXpDXyt7RjwxTX18bDNPKVdDbkt9VXE1LzBaWjE6OURyfTV6U09kalpnQzlrKEMgYU95bTZ1NVheXkBucXUsNHcxZylYaTMqNWs+dlApMHckRzNmSzdSLiE6cUNYTHcxPzV+I2gkREJTJnN2JldyaEk5TXpgL1tCRk82eXwqUXtJJGMmciZKZzcockVLVFlYJHxvZUY8aD1Ra04wRk0qRCgvKl01XlRXZTshQU9Sals6QDBKaGQ8QShWOStCVyt0KXtULnMzdSlRMjBXI248PjA3Jil7a0omWnBdSnYsZSwuXUoydkxUQWxLI1NkeVFTdmBbTU9VLiQ5altXcyh1SDN8d1NHfGIoR0E4WVd+b1glcX17cXlvWiNGP0RuKnVNSDIrdnFHNFlyc3pOeHFbbnB5bj8xQS97Vi0tJGN7a1BQLDx+JnJlL2ZsYEJtUEN0VHY5TFhaS01iRV1OW2lkVSp6RU9CdHRJVTt6IUJSNUshJl9ZWGw+c3lUeyl3bDdLN052PW1TKSxUfWNeOC88PWlmVFBvKzNxMltuVi0uYnRAKlQ6PGZ1cUw/ZSljSU1QQE9LU2VnN2FMc0N8S0MtLWtSIDFLd09ZRmQ5WnZ2b0E5Lmh1TU5NZ2pQQkNEVWhqeXg0YCldJV5WRTxsQH5HeEByIz49PjpSRFg+QFcjMiFtN20pfCtILnpKa3ptZSZ6e3pUKVI+OU1HUFAkT297UWBQPShFcSxdV00+a21LSUdeITE2V3Q4TWxFNj17Qig3K1l7QiBvdG1LYVlbOUFSRz8rNVd0PHRHLX1TQFk7RV9CeWM9fCZmRV5CNHoqXlBAX0ZYQjIkezZnTTI4SClKUWgzKEN0SX1uXjYpSXtgOXVET00sQS4sJVJhS2V8PXk5byhlfG5xWE4pTyo/WEd6Tn5IJjM+dSk2dF8xSzlfN0djcCYjQ3JMU09KMm9fPikgcWRRQEptOHw/L2BfWTdkY0FhVD5PbW5QYCUgUWdwKT9ZYE1yPmY+KXpaaVlZKGZzL00wQ2ErXSY+JEdpLnFlbyk9eS16Oi1KMT1kSjM5LzFqfD1ELV14QkhLQ3pCe251YSkjLWF6Rkk7VUhTdjh1UlJad05hbzxmMis0Vnd8a2xvKi0/QEcvKVIhMitQekMgfmx4KXxaKndYTFUvY1RGVWBrIDRCUzc+cD9MXS1dSSwwISt3KG5lKFdESC1hczJmbTVMfi9hdC9aPDtxS31+Z2ZkeWF0UnteR0ZvRExOQ2pyOlFuVSU/PyNffi5tSEIxQmxUaFhNUCZpdDJ1VmNeKzRzJl9XKCA9JWMjNyBfWFNlZ3NZfG9CdVRJNjljbW89UilNIUBeaHtvVmtmeXZdY3QpVEU3YilIPVsjfmF6fEpsPmNEZTE+W1ZAViR1U2hbYjdpa2wwQCxrQ19dVWl1U2hLcF57W155dm03XlRUVmEqQmJ9UURkUkV9PnB4K0ghaVB1bzJwK0R+dkQmcyh9WDY2ciVGZXhrYDBtbmNgXUdRc3x7M3U/VTdqUWxFaDgyQDJzeUtofXp9VTguPG8gZUI3al4sbjRtYExZSCk5UnY8YkM6eV57fSVfSl5YLU88JHVISSpxOV9wKWI9Sit9SHZyKiFfTXR2Vl9KaXp6RDNATF1UWShVX3F6ZlBgaDw1RG4lIzgzLGp9WXcudislfDhgeUs4LyptXzs1fVlvPkMuISBNQW0tSlBPPjxXNl8vVGNMSmc3dVlrZkI7VGZTXjwhaHlUJWVyPTxgL0cmNWdGZmRgJiBVPm8me35LVm9vdTQ9eGdJe0BnYFkvQDlsfm00IDQxOH5kMFlXUHg9NV0lREh0IVREZCAqI1koeWRaYnJ4Mio/KXFWbiMmSnxXQkMlY3ckVUV4O0c/dlI6a0pUXmozfDgzKGA/PUBuRT9zTHMqXWdgPTxHXU87c3BSanM6VWhRLz8kZEhGXS9oZEhMRVBFVjZocF4=",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
        }

        response = requests.post(url, headers=headers, data=payload)
        print("The resonse of token api is: ",response.text)
        res = response.json()
        # print("token is :",res['access_token'])
        return res['access_token']
    

    def create_passenger_list(self,adults_count, young_adults_count, children_count, infants_count):
        passengers = []
        
        # Add adults
        for _ in range(adults_count):
            passengers.append({"passengerTypeCode": "ADT"})
        
        # Add young adults
        for _ in range(young_adults_count):
            passengers.append({"passengerTypeCode": "B15"})
        
        # Add children
        for _ in range(children_count):
            passengers.append({"passengerTypeCode": "CHD"})
        
        # Add infants
        for _ in range(infants_count):
            passengers.append({"passengerTypeCode": "INF"})

        # print("the deatils of passengers are: ",passengers)
        
        return passengers
    

    def create_trip_itineraries(self,departure_date, origin_location, destination_location, trip_days=None):
        departure_date = datetime.strptime(departure_date, "%Y-%m-%d")
        
        # Outbound itinerary
        outbound_itinerary = {
            "departureDateTime": departure_date.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "originLocationCode": origin_location,
            "destinationLocationCode": destination_location,
            "isRequestedBound": True
        }
        
        itineraries = [outbound_itinerary]
        
        if trip_days is not None:
            # Return trip itinerary
            return_trip_date = departure_date + timedelta(days=trip_days)  
            return_trip_itinerary = {
                "departureDateTime": return_trip_date.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "originLocationCode": destination_location,
                "destinationLocationCode": origin_location,
                "isRequestedBound": False
            }
            itineraries.append(return_trip_itinerary)

        # print("the deatils of trip are: ",itineraries)
        
        
        return itineraries

    def get_ticket_class_code(self,ticket_class):
        class_mapping = {
            'eco': 'DEMALLFPP',
            'pre-eco': 'DEPALLFPP',
            'bus': 'DECALLFPP'
        }
        return class_mapping.get(ticket_class.lower(), 'Unknown')
    

    def swiss_air(self,adults_count, young_adults_count, children_count, infants_count,departure_date, origin_location, destination_location, trip_days=None):
        # if infants_count:
        #     if infants_count>adults_count:
        #         return "One Infant Per Adult is allowed"
        if infants_count > adults_count:
            raise ValueError("One Infant Per Adult is allowed")

            
        url = "https://api-shop.swiss.com//v1/one-booking/search/air-calendars"

        payload = json.dumps({
        "commercialFareFamilies": [
            "DECALLFPP"
        ],
        "travelers": self.create_passenger_list(adults_count, young_adults_count, children_count, infants_count),
        "itineraries": self.create_trip_itineraries(departure_date, origin_location, destination_location, trip_days),
        "searchPreferences": {
            "showUnavailableEntries": True,
            "showMilesPrice": False
        }
        })
        headers = {
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'callid': 'bce467df-c079-45ff-bff1-6d1effa6372f:1s',
        'sec-ch-ua-mobile': '?0',
        'authorization': f'Bearer {self.get_token()}',
        'akamai-bm-telemetry': 'a=3635805540034FFCDE6C800F12C8C166&&&e=NUI0RUY3NzQ3MEQ0MzFGOEE1RjRBNzZGMTEzNDUxNUV+WUFBUVhwNDJGNjFLc2VlT0FRQUE4bXNYR2hjb3RGWnZYMUJCc1JMS3laTEFqN2lybkIyZjdJQVhSSWFHdzFGVXJ5UnBOMklhcWhoOVI4U2xUZk9UalRlTk42OXQ1c3N3NjF0dlRVZTJEOFBmaWVMOVY5bm0rMmc1aUdWT3VtSWRxNHk2dHpINEZTQjJzMnNQY2ZnSkNEZTdmaTRteU4vK0VLRGVGQmtLQitkVFIxSGVHRWlxOG5qV21DV3dleW5CbDVIaFpxTHZycU1UbzVGOUE5c1lxV1JFQXM5TXZ6U05EZk81RVFRYWs4UlB5bC81U3ViWEw0M2xibGlXUXB6RmprK3ZnS2tzZ1g2dDhlMG9WU2RGNDUvN3RhaHRUQXdrdTlpVmVLUTRzNHdrNVh0eUwzTWlPcDhWYnNtYTNYRFg0RDJVNFVibjErU0NWMmxVUnExWlloWmtvbXRndFdHOXRJRGdjMWx5N2lndHFTRHlRNEdyWDZFUmJxcVdKS2E5cUVqbEhZQlJLVmY5MkhDeHZPVTJ3aE5jOXlKaEZoeWxkY241d3pLUTFjSEZURGIybnFnUEYyajlidFMzYkowanQyTThNL2tZWDNYbUwweUFpbE5PNUFwNi8wY0xCTWZKb2tRdE9KalBzVzNXZWc9PX40MzM3OTcwfjM1NTYxNTA=&&&sensor_data=Mjs0MzM3OTcwOzM1NTYxNTA7NCwzNSwwLDAsMiwxMzU7PSQrM2Q2ZkNDI3JEfTJadUMrXmNoMk8wJHFFTVt3KS5rWWx1QHxmP0sqeV89d0xmclc9SlslOCVWMF1Na0I9TkEqNF1ZKih3KCEsXlZeV3oxfWt4KGEpaz4yWElqQVNkW0doc1cuK3hNcHN3UmNvLW17Y0QyMThUK3RLOm1mMlQvXTxId3dxMWx6ajNsLERYKXYgbyBYKHdMVzkgTzdPeGJpKl1IfHtwKiYsIDZpYCxMP0VjLnJIPSUkWlc8fDFjVl8wWE4xMjBIQmJbX05MaTVESnAvc0Y0d3hbeyYmSCkpQ3dhLHcpLDxjLjA+I31HKSo3WktTMjYzOkNWPDNILzIrZlE6MlFJU15xUVlPUSVab3lWdm1fcFNDPzRUTXRMUGpPMSEgSE5zJENhdWVxSitDVSRaWkxQWGQ9UzUubmoxRXxYamEqOGh9SFF9dShpW2R+azpBMzAlSDJ8S0wkWk08KXJ2T2QgS2hMOWRibH1kLE0paHtQaGd2Uj0xPyhoX3RjTjFNOUwoTSE3bXgsbm0tT0gsKzZTYCAoUlRSQzlOLHxpJCVjc1EpU3lMbSBnYDpYTTZFUnkwU2YgKTswJU5tb2wwN3M+Yko5Wy5EZF1TNWRGQ1pgMD5tMlJgeG9jb2tyYSM9IUM7a0gpZ3ZERUB1R0w9UnlFVS5EbWF9Pmk6RlRRIEUhUUVwazd0R25ud00gMClUZj9gLlBlMFNNWVYgOHVJdFJHIWdKOX5VYHkgKD9ZPXE5aDB3PHdFbnswZU1kdlBna0pGeiZhQHFDU2VLKDZGczhxPDRfM2Q6NEk5cSFIfUd1WFU+QUFGckpdeWFSZ3pCd1IpbksqViE2Sz8pPGJIcW9UVENKOy5yT2ogcWcmL3A6KltSIW04JDNHS0JMa2YxKyQteDNwIF08XiUpfChFI1pJLiFYSX5hK0wsP2J3YEJRQkVUY1RUL2QtTHlxLVVEZ2BIPykmWz1hLX52S3ZvT2FOc2N+dyVtZzdbVlE2Vjk7UCA/Vz98XzlbWmM0YWlPVlt4ITkxRmo1LWQ5QXBoJW53bkEmLT04M142bURQUTRTX3krTyZdXiQuOXRLUi12MTxnNllmfkNTVV1sek4rS2R7bypFJENWck4tQEQpZVVBT1FlVmdSRSNeeS8gT2RadX5SZDNPbHB7VzxTZ0wzKXkpI2kmQy8pbEUoRS1xb3xxNmwpWiFDTih0OmF6aUJdLixBWSg/RjVtdS5KLTp5IU1gKlouLSUwX1VAbCx3ZlBdQUZ2cTR1I3BgI0s8PVJNLEE1UjdUITBGQTxtI3ZwSlEjVmt5RTo0KEpyN2tpIWU1WT1dUXdMaTJzIUF1amV3JERoJkZ4cyl8KE06OCpXcDd2TnpkSmsualdrIWNUN2Zhcm5FfE93UlJkKmNjPmF4RHFpLyRzKkU0JlI8UWs8VVFOYz9bQmpNLkpjak0+aiZXLGBZTkF8NUV1e2RHPmNgMWQ2WVQsNFcyS1ZsQixURTt2NkNlemx7YUlpdks/dUFbKzpNWUZMNEAwNGRDN2UtKGE7ZG1hOFBxJGIkamAmI2tAMikxSEFlLio0LGtLM3NWaU5efHIhbGNCaiw5KFN9eCt2XUQ/KGt9RzE/cCBqJGJXbjlAR0VCV197LnZfcnBVUmp7PkBgVD4wQiEpVU43b35TJlREM2VkKCR6aWJtME4+fitGbS0gd3hfRmBQJUp6MX4vdXxjQ0xUJSZ5RjAmOWc3Z2dzaTVnaGkvK1AjPWx9Tz1iSHZWSHZ0IHghJW1+JUVsUV54LXNKcip6ZDFSTVNZVXZbSVhoLHRpL2xDW3o8eCxtcGN9LCYmVkFmO0xEQ3Q+bSsxNV0xLDJaRSRyKiVpYS9nbX1Ke0ZXdWxjJnw/aFlyTHpDVDVjOSVyOHxtfSk8T3g+aW0qa0BxODBIOnptLH1sb0xEKnplR3t9eiwtbWh7JGYwXzgqKTYqYXxsUDJbQSVPOSRALjtNTiZDaiotRGcgQiRRX0YgbUFqejdhSGA9az54UTQ1ejYvIDEwTWMyP2phcmtPfEZNR1Z1Um17YzVgZm8sLipQLiNhITFOcz5MeyVAJiFdI34kQl84Z1d1ZkNzL09OUyBXVE5uc0doLlYhOlVDTStQVjlRVCxORnxxSy1CX2x1UygtLVFbNFAmRTM/X15jO3d4LF55YjkraGstfkRrfThoSVZSJThuNXlKdCxTX2xHLDQ9Jjw3cWhdPS53MXUkLShnYHhOYkpxWXxicVRWdFM2RFczYVQwQHQhYVsuaXI/d2R5fVh+aDMhWS1aOTdVSTNZY0NzcWZjT046PHRJayx6YXQyXTJ8VEt+YzNzJU0pekNgSyt6bHRwdFhnQSRNW2BWby5tNyhiXjovYDJNfGNjLFQ6cFdNLXsoXW03Xm1AOy5YdGE4KnNqSD10Y3JSQzZqKX5teGojK0UlQip5Qnd3eS9oSysjbGxZTH5tMkc3SyBBY1ZgZXUm',
        'content-type': 'application/json',
        'accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'cache-control': 'max-age=0',
        'ama-client-ref': 'bce467df-c079-45ff-bff1-6d1effa6372f:1s',
        'sec-ch-ua-platform': '"Windows"',
        'host': 'api-shop.swiss.com',
        'Cookie': '_abck=3635805540034FFCDE6C800F12C8C166~0~YAAQ5CEPF+ZzxeyOAQAASBFYIAvaC4N1JdNyimp2p7j8dIdqCuiHIa+g55DbM4JtetGwKM1UtsvTz4fEDcZ7W0G0RjIa1IOqhaDMS0xE80yvCxt7Tp2dEH3kQiN0D3KdvWERao7d1SZqAU9iBRyF9koAE/k9tkRCo51C0LP+qUqxLElyP5jj3u+mXwFUMK2BwNoJIyNZM45gvDYv97VEbG2sWvopAKm+4TOEc0QCGRyWxRbABEIBZSnH88sPPTLSdymdeVXbeUwmGbJ5anMr7RAsQvOlPYhSgg+0/ivIx4X5OJhlnbH4flLucK/Opf4usSfqMJm7fRmprSb5TvhF7Svfcmqr5JaWrnWpUe3WGAMcUEuZbpoJKlkYqiJ1tv3AAYCDReVH/wGInLfAr12S2lBzcdFsmxRGqqHhulSz10ltd6KyI8HqU8wAD5Wgtxo0tsYw40CHhSw=~-1~-1~-1; bm_mi=A5E1990C5DD35AF7401C0D6E889F149E~YAAQ5CEPF+dzxeyOAQAASBFYIBdKiyLYz3fxtLI9gkY1myoDv765w4Jq/J5m0Wvp0obReTMYtY2/twCNG0yhmdnoH80x9Zk0or+16R2PdXr1KPuDE7TLMxrypJ3+N5Q6Qpy1bfjgGiatgj+UBOHJs140qkrPt5oy/ZBDGp0LC57brAVus57Hupq/bRhBRB5I32eOSvdZPUaFcoG3drBrvGeCxC3ZP3h1w44J8MXT8QeH7nTmvtXuxc7h4z+3qANdtx3RyPw3XjEmsy6tkfSi8XFKZAw4uxU+7DAcwls5APJEmWb9kyP7ixtq5npbH881oGvWH4bPwpi1nezlKrW50eQ=~1; bm_sz=2B62B6380E10C80EDAF95CCF671E1494~YAAQ5CEPF+lzxeyOAQAASBFYIBcS3HKEcTYXOt/QVkDhjE3eMObIgVtizCLe1mxhpnaxmioeVxL2vcQ6xy/c0OpO3rzv6xWcF05d8cOqxiuAHccji4Bi4LAUe/W1DP1xf6piS0+1MtuDocK8ZZAi487lWdgo3UFS/TGJ1BzJ6D9Qb0g/EGaLN1oL7wQCXDLmrGeYB6ZY7zf6ytvO0KyO+Eg4RoilLcjocVyB8F2VFFvp67Mj1J/3oeB+Ws9n8zNEzFkX1Jdl4KsoBvxunS1EKoBUBJN88y5OK6OfNy0Xa+7Qvy4RusAA8JHMtt32xb22XszBMhjG/UqIUiE2ScmOTGOUGHq4DWpEQ2ZUNU6hqbrQEoDZT+WWr1eVxrZQZn/yYT3ia1TRTJDKAKM6CA2npwdlIHYgbEw4con0BdU0ZLreXxa0Zf/QZUs=~3687992~4535091; utag_main=v_id:018f0b2b744b000241753b46c9200506f003306700978$_sn:7$_se:7$_ss:0$_st:1714236394809$dc_visit:7$ses_id:1714234562447%3Bexp-session$_pn:3%3Bexp-session$dc_event:5%3Bexp-session; searchFlightHistory=%5B%7B%22from%22%3A%22LHR%22%2C%22to%22%3A%22FRA%22%2C%22departureDate%22%3A%2220240520%22%2C%22tripType%22%3A%22O%22%2C%22nbAdt%22%3A1%2C%22nbChd%22%3A0%2C%22nbInf%22%3A0%2C%22cabin%22%3A%22E%22%2C%22airline%22%3A%22LH%22%7D%2C%7B%22from%22%3A%22LHR%22%2C%22to%22%3A%22FRA%22%2C%22departureDate%22%3A%2220240429%22%2C%22tripType%22%3A%22O%22%2C%22nbAdt%22%3A2%2C%22nbChd%22%3A0%2C%22nbInf%22%3A0%2C%22cabin%22%3A%22E%22%2C%22airline%22%3A%22LH%22%7D%2C%7B%22from%22%3A%22LHR%22%2C%22to%22%3A%22FRA%22%2C%22departureDate%22%3A%2220240429%22%2C%22tripType%22%3A%22O%22%2C%22nbAdt%22%3A1%2C%22nbChd%22%3A0%2C%22nbInf%22%3A0%2C%22cabin%22%3A%22E%22%2C%22airline%22%3A%22LH%22%7D%2C%7B%22from%22%3A%22LHR%22%2C%22to%22%3A%22FRA%22%2C%22departureDate%22%3A%2220240429%22%2C%22tripType%22%3A%22O%22%2C%22nbAdt%22%3A1%2C%22nbChd%22%3A0%2C%22nbInf%22%3A0%2C%22cabin%22%3A%22F%22%2C%22airline%22%3A%22LH%22%7D%5D; bm_sv=9D6C6CCF581A259773790B1AD47AB832~YAAQ5CEPF/lzxeyOAQAAYBdYIBdnqd9s0KJK6JVSXglzbYFU3C5tiOhLuBmitYVJpFuHC/BpPvY/ns++mGgnnRbXuk6sLXuXRZbtD83mVN+nKYY60GKU1q5XWvM+CSekhviV8rWsW0l4F+lRW1ZM9Pca7qO23+DFT3LonamRMlQ0uK2mSRwBwvakvgT9ZM6MTlhFe4mbblSr+sVvpn5bQWAYvSl6wgooOavGLg0YoALiRXGKJT4L+hbyHpb9Uaw+~1; ak_bmsc=B305DB8D53AC09DD695F8FB207F23F4B~000000000000000000000000000000~YAAQ5CEPF/pzxeyOAQAAsRdYIBcpn9wvenSLUMgElDBCEMJFgrX9urnK5onuSTaJTotiUmKc2JYghkUbFvvRe6uUrque2sariqb3fvSWvGVihcLJGanC/ER1F5CfniX9jU8bet7vcZbIkxj7qpi7oGdtepSO9x8srJLRjNf8lv9DstSNJUgV3NWUrmRpsIg1vjVBJ4E2djJ3XDB+o3AqTfTXWh2hz354sQ+Z+vXax2Q25ajZxTRwMahyRVo++ZodfF4i4r2n7AypNj0eEAYIjlf13L/mIf70NjFixgb38iA1hL0nF763ZWgAfIZOBVrO6obYwE8SFs5qLPI5BnTv9ZKRMHBUuH9aWh5a5pL/RXWKux5yf4G+yib0bwswfnEwNXHTECMSVOnDZw=='
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        # print("The swiss function response is :", response.text)
        return response.json()

    # print(response.text)