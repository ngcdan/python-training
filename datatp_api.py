import requests

api_url = 'http://localhost:7080/rest/v1.0.0/account/profile/dan?'  # Điều chỉnh URL này để phù hợp với API của bạn

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        # Xử lý dữ liệu từ API response
        data = response.json()
        print(data)
    else:
        print(f"Không thể gọi API, mã lỗi: {response}")
except Exception as e:
    print(f"Lỗi khi gọi API: {e}")

