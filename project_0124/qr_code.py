import qrcode 
from PIL import Image

# # generating QR from UPI ID
# upi_number = input("Enter Your UPI number = ")
# # print("Choose Your UPI Handle @ybl / @ibl / @axl / @okhdfcbank / @oksbi / @okicici/  @okaxis")

# Define the list of UPI handles
upi_handles = [
    "@ybl",
    "@ibl",
    "@axl",
    "@okhdfcbank",
    "@oksbi",
    "@okicici",
    "@okaxis"
]

# # Print the available UPI handles
# print("Choose Your UPI Handle:")
# for i, handle in enumerate(upi_handles, 1):
#     print(f"{i}. {handle}")

# # Get user input for the chosen handle
# selected_index = int(input("Enter the number corresponding to your choice: "))

# # Validate the user input
# if 1 <= selected_index <= len(upi_handles):
#     selected_handle = upi_handles[selected_index - 1]
#     print(f"You selected: {selected_handle}")
#     upi_number_with_handle = f"{upi_number}{selected_handle}"
#     print(f"Complete UPI ID: {upi_number_with_handle}")
# else:
#     print("Invalid choice. Please enter a valid number.")

# # format for any transaction
# '''
# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
# pa = person upi jisko transfer krna hai
# pn = person name jisko transfer krna hai
# am = amount
# cu = currency
# tn = thankyou note/message
# mc = merchant code
# ''' 

# phone_pay_url = f'upi://pay?pa={upi_number_with_handle}&pn=Recipient%20NAME&mc1234'
# google_pay_url = f'upi://pay?pa={upi_number_with_handle}&pn=Recipient%20NAME&mc1234'

# # making QR
# phone_pay_qr = qrcode.make(phone_pay_url)
# google_pay_qr = qrcode.make(google_pay_url)

# # Saving QR Images
# phone_pay_qr.save('phonepay_qr.png')
# google_pay_qr.save('googlepay_qr.png')

# # PIL(pillow library) lib used for diaplay image
# phone_pay_qr.show()
# google_pay_qr.show()
# # Image.open('phonepay_qr.png').show()
# # Image.open('googlepay_qr.png').show()


def generate_phonepay_qr(upi_number,phonepay_handle):
    phonepay_url = f'upi://pay?pa={upi_number}{phonepay_handle}&pn=Recipient%20NAME&mc1234'
    phonepay_qr = qrcode.make(phonepay_url)
    phonepay_qr.save('phonepay_qr.png')
    print("PhonePe QR code generated successfully.")
    # PIL(pillow library) lib used for diaplay image
    phonepay_qr.show()

def generate_googlepay_qr(upi_number,googlepay_handle):
    googlepay_url = f'upi://pay?pa={upi_number}{googlepay_handle}&pn=Recipient%20NAME&mc1234'
    googlepay_qr = qrcode.make(googlepay_url)
    googlepay_qr.save('googlepay_qr.png')
    print("Google Pay QR code generated successfully.")
    googlepay_qr.show()

# UPI number input from the user
upi_number = input("Enter Your UPI number = ")

# Print the available UPI handles
print("Choose Your UPI Handle:")
for i, handle in enumerate(upi_handles, 1):
    print(f"{i}. {handle}")

# Get user input for the chosen handle
selected_index = int(input("Enter the number corresponding to your choice: "))

# Validate the user input
if 1 <= selected_index <= len(upi_handles):
    selected_handle = upi_handles[selected_index - 1]

    # Check if the selected handle belongs to PhonePe or Google Pay
    if selected_handle in ["@ybl", "@ibl", "@axl"]:
        generate_phonepay_qr(upi_number,selected_handle)
    elif selected_handle in ["@okhdfcbank", "@oksbi", "@okicici", "@okaxis"]:
        generate_googlepay_qr(upi_number,selected_handle)
    else:
        print("Invalid handle.")
else:
    print("Invalid choice. Please enter a valid number.")
