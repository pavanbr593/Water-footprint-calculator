import streamlit as st

# Translations for multiple languages
translations = {
    "en": {
        "title": "🌾💧 Water Footprint Calculator",
        "description": "**Water Footprint Calculator** helps you estimate the water footprint for various agricultural products and final products.",
        "features": "### Features:\n- **Calculate Water Footprint for Raw Products**: Input crop type, region, and quantity.\n- **Calculate Water Footprint for Final Products**: Input the final product and quantity.",
        "supported_products": "### Supported Products:\n- **Raw Products**: Wheat, Rice, Corn, Soybean\n- **Final Products**: Bottled Orange Juice, Cooked Rice, Steamed Tomato, Canned Beans",
        "regions": "### Regions:\nCovers all states of India.",
        "how_to_use": "### How to Use:\n1. **Select the Product Type**: Raw or Final.\n2. **Input the Required Information**.\n3. **Click Calculate**.",
        "developed_by": "Developed by BitByBit",
        "product_types": ["Raw", "Final Product"],
        "raw_products": ["Wheat", "Rice", "Corn", "Soybean"],
        "final_products": ["Bottled Orange Juice", "Cooked Rice", "Steamed Tomato", "Canned Beans"],
        "calculate": "Calculate",
        "error_message": "Please enter all fields with valid values.",
    },
    "hi": {
        "title": "🌾💧 जल पदचिह्न कैलकुलेटर",
        "description": "**जल पदचिह्न कैलकुलेटर** आपको विभिन्न कृषि उत्पादों और अंतिम उत्पादों के लिए जल पदचिह्न का अनुमान लगाने में मदद करता है।",
        "features": "### सुविधाएँ:\n- **कच्चे उत्पादों के लिए जल पदचिह्न की गणना करें**: फसल प्रकार, क्षेत्र और मात्रा इनपुट करें।\n- **अंतिम उत्पादों के लिए जल पदचिह्न की गणना करें**: अंतिम उत्पाद और मात्रा दर्ज करें।",
        "supported_products": "### समर्थित उत्पाद:\n- **कच्चे उत्पाद**: गेहूं, चावल, मक्का, सोयाबीन\n- **अंतिम उत्पाद**: बोतलबंद संतरे का रस, पका हुआ चावल, स्टीम्ड टमाटर, कैन्ड बीन्स",
        "regions": "### क्षेत्र:\nभारत के सभी राज्य कवर किए गए हैं।",
        "how_to_use": "### उपयोग कैसे करें:\n1. **उत्पाद प्रकार चुनें**: कच्चा या अंतिम।\n2. **आवश्यक जानकारी दर्ज करें**।\n3. **कैल्क्युलेट बटन पर क्लिक करें**।",
        "developed_by": "BitByBit द्वारा विकसित",
        "product_types": ["कच्चा", "अंतिम उत्पाद"],
        "raw_products": ["गेहूं", "चावल", "मक्का", "सोयाबीन"],
        "final_products": ["बोतलबंद संतरे का रस", "पका हुआ चावल", "स्टीम्ड टमाटर", "कैन्ड बीन्स"],
        "calculate": "गणना करें",
        "error_message": "कृपया सभी फ़ील्ड में मान्य मान दर्ज करें।",
    },
    "ta": {
        "title": "🌾💧 நீர் காலடிக்குறிப்பு கணக்கீடு",
        "description": "**நீர் காலடிக்குறிப்பு கணக்கீடு** வேளாண் மற்றும் இறுதிப் பொருட்களுக்கு நீர் காலடிக்குறிப்பு மதிப்பீடு செய்ய உதவுகிறது.",
        "features": "### அம்சங்கள்:\n- **முதன்மை பொருட்கள்**: பயிர் வகை, பகுதி, அளவு அளிக்கவும்.\n- **இறுதிப் பொருட்கள்**: இறுதி பொருள் மற்றும் அளவை அளிக்கவும்.",
        "supported_products": "### ஆதரவு பொருட்கள்:\n- **முதன்மை பொருட்கள்**: கோதுமை, அரிசி, மக்காச்சோளம், சோயாபீன்\n- **இறுதிப் பொருட்கள்**: பாட்டிலில் ஆரஞ்சு சாறு, சமைத்த அரிசி, ஆவியூட்டிய தக்காளி, கேன்டு பீன்ஸ்",
        "regions": "### பகுதி:\nஇந்தியாவின் அனைத்து மாநிலங்களையும் உள்ளடக்கியது.",
        "how_to_use": "### பயன்பாடு:\n1. **தயாரிப்பு வகை தேர்வு செய்யவும்**: முதன்மை அல்லது இறுதி.\n2. **தேவையான தகவலை அளிக்கவும்**.\n3. **கணக்கீடு கிளிக் செய்யவும்**.",
        "developed_by": "BitByBit மூலம் உருவாக்கப்பட்டது",
        "product_types": ["முதன்மை", "இறுதி பொருட்கள்"],
        "raw_products": ["கோதுமை", "அரிசி", "மக்காச்சோளம்", "சோயாபீன்"],
        "final_products": ["பாட்டிலில் ஆரஞ்சு சாறு", "சமைத்த அரிசி", "ஆவியூட்டிய தக்காளி", "கேன்டு பீன்ஸ்"],
        "calculate": "கணக்கிடு",
        "error_message": "சரியான மதிப்புகளை உள்ளிடவும்.",
    },
    "te": {
        "title": "🌾💧 నీటి ఆనవాళ్ల క్యాలిక్యులేటర్",
        "description": "**నీటి ఆనవాళ్ల క్యాలిక్యులేటర్** వ్యవసాయ ఉత్పత్తులు మరియు తుది ఉత్పత్తుల నీటి వినియోగాన్ని అంచనా వేయడంలో సహాయపడుతుంది.",
        "features": "### లక్షణాలు:\n- **ముడి ఉత్పత్తుల నీటి వినియోగం**: పంట రకం, ప్రాంతం మరియు పరిమాణం ఇవ్వండి.\n- **తుది ఉత్పత్తుల నీటి వినియోగం**: తుది ఉత్పత్తి మరియు పరిమాణాన్ని ఇవ్వండి.",
        "supported_products": "### మద్దతు ఉత్పత్తులు:\n- **ముడి ఉత్పత్తులు**: గోధుమ, బియ్యం, మొక్కజొన్న, సోయాబీన్\n- **తుది ఉత్పత్తులు**: బాటిల్ ఆరెంజ్ జ్యూస్, ఉడికించిన బియ్యం, ఆవిరి టమోటా, డబ్బాలో బీన్స్",
        "regions": "### ప్రాంతాలు:\nభారతదేశంలోని అన్ని రాష్ట్రాలు కవర్ చేయబడ్డాయి.",
        "how_to_use": "### ఎలా ఉపయోగించాలి:\n1. **ఉత్పత్తి రకం ఎంచుకోండి**: ముడి లేదా తుది ఉత్పత్తులు.\n2. **అవసరమైన సమాచారం ఇవ్వండి**.\n3. **క్యాలిక్యులేట్ క్లిక్ చేయండి**.",
        "developed_by": "BitByBit ద్వారా అభివృద్ధి చేయబడింది",
        "product_types": ["ముడి", "తుది ఉత్పత్తి"],
        "raw_products": ["గోధుమ", "బియ్యం", "మొక్కజొన్న", "సోయాబీన్"],
        "final_products": ["బాటిల్ ఆరెంజ్ జ్యూస్", "ఉడికించిన బియ్యం", "ఆవిరి టమోటా", "డబ్బాలో బీన్స్"],
        "calculate": "క్యాలిక్యులేట్",
        "error_message": "దయచేసి అన్ని ఫీల్డ్స్‌లో చెల్లుబాటు అయ్యే విలువలు నమోదు చేయండి.",
    },
    "kn": {
        "title": "🌾💧 ನೀರಿನ ಪಾದಚಿಹ್ನೆಗಳ ಕ್ಯಾಲಿಕ್ಯುಲೇಟರ್",
        "description": "**ನೀರಿನ ಪಾದಚಿಹ್ನೆಗಳ ಕ್ಯಾಲಿಕ್ಯುಲೇಟರ್** ವಿವಿಧ ಕೃಷಿ ಉತ್ಪನ್ನಗಳು ಮತ್ತು ಅಂತಿಮ ಉತ್ಪನ್ನಗಳ ನೀರಿನ ಬಳಕೆಯನ್ನು ಅಂದಾಜಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "features": "### ವೈಶಿಷ್ಟ್ಯಗಳು:\n- **ಮೂಲ ಉತ್ಪನ್ನಗಳು**: ಬೆಳೆ ಪ್ರಕಾರ, ಪ್ರದೇಶ ಮತ್ತು ಪ್ರಮಾಣವನ್ನು ನಮೂದಿಸಿ.\n- **ಅಂತಿಮ ಉತ್ಪನ್ನಗಳು**: ಅಂತಿಮ ಉತ್ಪನ್ನ ಮತ್ತು ಪ್ರಮಾಣವನ್ನು ನಮೂದಿಸಿ.",
        "supported_products": "### ಬೆಂಬಲಿತ ಉತ್ಪನ್ನಗಳು:\n- **ಮೂಲ ಉತ್ಪನ್ನಗಳು**: ಗೋಧಿ, ಅಕ್ಕಿ, ಜೋಳ, ಸೋಯಾಬೀನ್\n- **ಅಂತಿಮ ಉತ್ಪನ್ನಗಳು**: ಬಾಟಲ್ ಆರೇಂಜ್ ಜ್ಯೂಸ್, ಅಕ್ಕಿಯನ್ನು ಒದ್ದಾಗಿ, ಆವಿಯಿ ಟೊಮ್ಯಾಟೊ, ಕ್ಯಾನ್ಡ್ ಬೀನ್ಸ್",
        "regions": "### ಪ್ರದೇಶಗಳು:\nಭಾರತದ ಎಲ್ಲಾ ರಾಜ್ಯಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.",
        "how_to_use": "### ಬಳಸುವುದು ಹೇಗೆ:\n1. **ಉತ್ಪನ್ನದ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ**: ಮೂಲ ಅಥವಾ ಅಂತಿಮ.\n2. **ಅಗತ್ಯವಿರುವ ಮಾಹಿತಿ ನಮೂದಿಸಿ**.\n3. **ಕ್ಯಾಲಿಕ್ಯುಲೇಟರ್ ಕ್ಲಿಕ್ ಮಾಡಿ**.",
        "developed_by": "BitByBit ಮೂಲಕ ಅಭಿವೃದ್ಧಿಪಡಿಸಲಾಗಿದೆ",
        "product_types": ["ಮೂಲ", "ಅಂತಿಮ ಉತ್ಪನ್ನಗಳು"],
        "raw_products": ["ಗೋಧಿ", "ಅಕ್ಕಿ", "ಜೋಳ", "ಸೋಯಾಬೀನ್"],
        "final_products": ["ಬಾಟಲ್ ಆರೇಂಜ್ ಜ್ಯೂಸ್", "ಅಕ್ಕಿಯನ್ನು ಒದ್ದಾಗಿ", "ಆವಿಯಿ ಟೊಮ್ಯಾಟೊ", "ಕ್ಯಾನ್ಡ್ ಬೀನ್ಸ್"],
        "calculate": "ಕ್ಯಾಲಿಕ್ಯುಲೇಟರ್",
        "error_message": "ಸಕಾಲಿಕ ಮೌಲ್ಯಗಳನ್ನು ನಮೂದಿಸಿ.",
    },
    "mr": {
        "title": "🌾💧 पाण्याचा ठसा कॅल्क्युलेटर",
        "description": "**पाण्याचा ठसा कॅल्क्युलेटर** विविध शेती उत्पादने आणि अंतिम उत्पादने यांचे पाण्याचा वापर मोजण्यास मदत करतो.",
        "features": "### वैशिष्ट्ये:\n- **मूलभूत उत्पादने**: पिकाचा प्रकार, क्षेत्र आणि प्रमाण निवडा.\n- **अंतिम उत्पादने**: अंतिम उत्पादन आणि प्रमाण निवडा.",
        "supported_products": "### समर्थीत उत्पादने:\n- **मूलभूत उत्पादने**: गहू, तांदूळ, मका, सोयाबीन\n- **अंतिम उत्पादने**: बाटलीत ऑरेंज ज्यूस, शिजलेले तांदूळ, वाफवलेले टोमॅटो, कॅन्ड बीन्स",
        "regions": "### क्षेत्र:\nभारताच्या सर्व राज्यांचे कव्हरेज केले आहे.",
        "how_to_use": "### वापरण्याची पद्धत:\n1. **उत्पादन प्रकार निवडा**: मूलभूत किंवा अंतिम उत्पादने.\n2. **आवश्यक माहिती भरा**.\n3. **कॅल्क्युलेटर क्लिक करा**.",
        "developed_by": "BitByBit द्वारे विकसित केलेले",
        "product_types": ["मूलभूत", "अंतिम उत्पादने"],
        "raw_products": ["गहू", "तांदूळ", "मका", "सोयाबीन"],
        "final_products": ["बाटलीत ऑरेंज ज्यूस", "शिजलेले तांदूळ", "वाफवलेले टोमॅटो", "कॅन्ड बीन्स"],
        "calculate": "गणना करा",
        "error_message": "सर्व फील्ड्समध्ये योग्य मूल्ये भरा.",
    }
}

# List of Indian States and Region-Specific Multipliers for Water Footprint
states = {
    "Andhra Pradesh": 1.05,
    "Arunachal Pradesh": 1.1,
    "Assam": 1.15,
    "Bihar": 0.95,
    "Chhattisgarh": 0.9,
    "Goa": 1.0,
    "Gujarat": 0.85,
    "Haryana": 1.2,
    "Himachal Pradesh": 0.95,
    "Jharkhand": 0.9,
    "Karnataka": 1.05,
    "Kerala": 1.1,
    "Madhya Pradesh": 0.85,
    "Maharashtra": 0.9,
    "Manipur": 1.15,
    "Meghalaya": 1.1,
    "Mizoram": 1.15,
    "Nagaland": 1.1,
    "Odisha": 0.95,
    "Punjab": 1.25,
    "Rajasthan": 1.3,
    "Sikkim": 1.1,
    "Tamil Nadu": 1.05,
    "Telangana": 1.1,
    "Tripura": 1.15,
    "Uttar Pradesh": 1.2,
    "Uttarakhand": 1.0,
    "West Bengal": 1.0,
    "Delhi": 1.15,
    "Puducherry": 1.05,
    "Lakshadweep": 1.1,
    "Andaman and Nicobar Islands": 1.1,
    "Chandigarh": 1.2,
    "Dadra and Nagar Haveli and Daman and Diu": 1.05,
    "Jammu and Kashmir": 0.95,
    "Ladakh": 1.05,
}

# Initialize session state for language if not set
def main():
    # Set default language as English
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    
    # Sidebar to select language
    language = st.sidebar.selectbox(
        'Select Language',
        ['English', 'हिन्दी', 'தமிழ்', 'తెలుగు', 'ಕನ್ನಡ', 'मराठी']
    )

# Language selection
st.sidebar.title("Select Language")
selected_language = st.sidebar.radio(
    "Choose a language / भाषा चुनें / மொழி தேர்வு செய்யவும் / ఎంచుకోండి", 
    ("English", "हिन्दी", "தமிழ்", "తెలుగు", "ಕನ್ನಡ","मराठी"), 
    format_func=lambda lang: lang
)

# Set language in session state based on selection
language_map = {
        'English': 'en',
        'हिन्दी': 'hi',
        'தமிழ்': 'ta',
        'తెలుగు': 'te',
        'ಕನ್ನಡ': 'kn',
        'मराठी': 'mr'
}
st.session_state.language = language_map[selected_language]

# Main function
def main():
    # Display the logo
    st.title(translations[st.session_state.language]["title"])

    # Sidebar for app description and guide
    st.sidebar.header(translations[st.session_state.language]["description"])
    st.sidebar.write(translations[st.session_state.language]["features"])
    st.sidebar.write(translations[st.session_state.language]["supported_products"])
    st.sidebar.write(translations[st.session_state.language]["regions"])
    st.sidebar.write(translations[st.session_state.language]["how_to_use"])
    st.sidebar.write(translations[st.session_state.language]["developed_by"])

    # Product type selection
    product_type = st.selectbox(
        "Select Product Type",
        translations[st.session_state.language]["product_types"]
    )

    # Input fields for raw products
    if product_type == translations[st.session_state.language]["product_types"][0]:  # "Raw"
        crop_type = st.selectbox(
            "Select Crop Type",
            translations[st.session_state.language]["raw_products"]
        )
        region = st.selectbox("Select Region", list(states.keys()))
        quantity = st.number_input("Enter Quantity (in kg)", min_value=0.0, step=0.1)

        # Calculation logic for raw products
        def calculate_water_footprint(crop, region, quantity):
            water_footprints = {
                "Wheat": 1000,       # liters per kg
                "Rice": 2000,        # liters per kg
                "Corn": 1500,        # liters per kg
                "Soybean": 1200,     # liters per kg
                "Barley": 1420,      # liters per kg
                "Oats": 1400,        # liters per kg
                "Peanuts": 3100,     # liters per kg
                "Cottonseed": 3400,  # liters per kg
                "Sunflower": 2800,   # liters per kg
                "Sugarcane": 1500,   # liters per kg
                "Almonds": 16000,    # liters per kg
                "Coffee Beans": 18000,  # liters per kg

            }
            regional_multiplier = states[region]  # Get multiplier for the selected region
            return water_footprints.get(crop, 0) * quantity * regional_multiplier

        # Calculate and display results
        if st.button(translations[st.session_state.language]["calculate"]):
            if crop_type and region and quantity > 0:
                water_footprint = calculate_water_footprint(crop_type, region, quantity)
                st.write(f"**Water Footprint for {quantity} kg of {crop_type} in {region}: {water_footprint} liters**")
            else:
                st.write(translations[st.session_state.language]["error_message"])

    else:  # "Final"
        final_product = st.selectbox(
            "Select Final Product",
            translations[st.session_state.language]["final_products"]
        )
        quantity = st.number_input("Enter Quantity (in kg)", min_value=0.0, step=0.1)

        # Simple calculation logic for final products
        def calculate_final_product_water_footprint(product, region, quantity):
            product_water_footprints = {
                "Bottled Orange Juice": 2500,    # liters per kg
                "Cooked Rice": 1500,             # liters per kg
                "Steamed Tomato": 800,           # liters per kg
                "Canned Beans": 1200 ,           # liters per kg
                "Bottled Orange Juice": 2500,     # liters per kg
                "Bread (Wheat)": 1600,            # liters per kg
                "Boiled Pasta": 1900,             # liters per kg
                "Chocolate Bar": 17000,           # liters per kg
                "Grilled Beef": 15400,            # liters per kg
                "Roast Chicken": 4300,            # liters per kg
                "Mashed Potatoes": 287,           # liters per kg
                "Baked Apples": 822,              # liters per kg
                "Bottled Milk": 1000,             # liters per kg
               "Sliced Cheese": 5000,            # liters per kg
               "Boiled Eggs": 3300,              # liters per kg

            }
            regional_multiplier = states[region]  # Get multiplier for the selected region
            return product_water_footprints.get(product, 0) * quantity * regional_multiplier

        # Calculate and display results
        if st.button(translations[st.session_state.language]["calculate"]):
            if final_product and quantity > 0:
                water_footprint = calculate_final_product_water_footprint(final_product, region, quantity)
                st.write(f"**Water Footprint for {quantity} kg of {final_product} in {region}: {water_footprint} liters**")
            else:
                st.write(translations[st.session_state.language]["error_message"])

if __name__ == "__main__":
    main()
