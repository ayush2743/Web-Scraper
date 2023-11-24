import requests
from bs4 import BeautifulSoup

# URL of the Amazon product page
url = input("Enter the Amazon Product link : ")
head = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language' : 'en-US, en;q=0.5'})


# Send an HTTP request to the URL
response = requests.get(url, headers=head)



# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find("span", attrs={'id':'productTitle'})
    print(title.text.strip())
    
    
    price = soup.find("span", attrs={'class':'a-price-whole'})
    print("₹",price.text.strip())
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


    
# URL of the Flipkart product page
url = input("Enter the Flipkart Product link : ")
head = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language' : 'en-US, en;q=0.5'})


# Send an HTTP request to the URL
response = requests.get(url, headers=head)



# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find("span", attrs={'class':'B_NuCI'})
    print(title.text.strip())
    
    
    price = soup.find("div", attrs={'class':'_30jeq3 _16Jk6d'})
    print("₹",price.text.strip())
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
