import vobject

def extract_numbers_and_names(vcf_file_path):
    with open(vcf_file_path, 'r', encoding='utf-8') as vcf_file:
        vcard_str = vcf_file.read()

    vcards = vobject.readComponents(vcard_str)

    names = []
    numbers = []

    for vcard in vcards:
        if vcard:
            # Extracting the first phone number from different fields
            phone_number = None

            if hasattr(vcard, 'tel') and vcard.tel.value:
                phone_number = vcard.tel.value

            elif hasattr(vcard, 'item1') and 'TEL' in vcard.item1.params:
                phone_number = vcard.item1.TEL.value

            elif hasattr(vcard, 'item2') and 'TEL' in vcard.item2.params:
                phone_number = vcard.item2.TEL.value

            # If a phone number is found, add it to the list
            if phone_number:
                numbers.append(phone_number)
            
            # Extracting names
            if hasattr(vcard, 'fn') and vcard.fn.value:
                names.append(vcard.fn.value)

    return names, numbers

# Provide the file path
vcf_file_path = 'assets/vCards.vcf'

# Extract names and numbers
names, numbers = extract_numbers_and_names(vcf_file_path)

# Display the results
# if names and numbers:
#     print("Names:", names)
#     print("Numbers:", numbers)

with open('phone_numbers.txt', 'w') as file:
    for number in numbers:
        file.write(number + '\n')

