import streamlit as st

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius": 
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"Meters": 1.0, "Kilometers": 1000.0, "Miles": 1609.34, "Feet": 0.3048, "Inches": 0.0254},
        "Mass": {"Kilograms": 1.0, "Grams": 0.001, "Pounds": 0.453592},
        "Area": {"Square Meters": 1.0, "Square Kilometers": 1e6, "Square Miles": 2.59e6, "Hectares": 1e4, "Acres": 4046.86},
        "Volume": {"Liters": 1.0, "Milliliters": 0.001, "Cubic Meters": 1000.0},
        "Time": {"Seconds": 1.0, "Minutes": 60.0, "Hours": 3600.0, "Days": 86400.0},
        "Speed": {"Meters per second": 1.0, "Kilometers per hour": 0.277778, "Miles per hour": 0.44704},
        "Pressure": {"Pascals": 1.0, "Bars": 1e5, "Atmospheres": 101325},
        "Energy": {"Joules": 1.0, "Kilojoules": 1000.0, "Calories": 4.184},
        "Frequency": {"Hertz": 1.0, "Kilohertz": 1000.0, "Megahertz": 1e6},
        "Plane Angle": {"Degrees": 1.0, "Radians": 57.2958},
        "Fuel Economy": {"Miles per gallon": 1.0, "Kilometers per liter": 2.35215},
        "Data Transfer Rate": {"Bits per second": 1.0, "Kilobits per second": 1000.0},
        "Digital Storage": {"Bytes": 1.0, "Kilobytes": 1024.0, "Megabytes": 1048576.0},
        "Weight": {"Kilograms": 1.0, "Grams": 0.001, "Pounds": 0.453592}
    }
    
    if category in conversion_factors and isinstance(conversion_factors[category], dict):
        return (value / conversion_factors[category][from_unit]) * conversion_factors[category][to_unit]
    elif category == "Temperature":
        return temperature_converter(value, from_unit, to_unit)
    return value

# import streamlit as st 
st.markdown(
    """
     <style>
     body {
     background-color:  #f0f2f6;
     color: white;
    }
     .stApp {
     background: linear-gradient(1135deg, #bcbcbc, #cfe2f3);
     padding: 30px;
     border-radius: 15px;
     box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
   
    }
    h1 {
      text-align: center;
      font-size: 36px;
      color: white;
    }
    .stButton>button {
      background: linear-gradient(45deg, #0b5394, #351c75);
      color: white;
      font-size: 18px;
      padding: 10px 20px;
      border-radius: 10px;
      transition:  0.3s;
      box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
     
    .stButton>button:hover {
     transform: scale(1.05);
     background: linear-gradient(45deg, #0b5394, #351c75);
     color: black
    }

    .result-box {
     font-size: 20px;
     font-weight: bold;
     text-align: center;
     padding: 25px;
     border-radius: 10px;
     background-color: rgba(255, 255, 255, 0.1);
     box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }

    .footer{
     text-align: center;
     font-size: 14px;
     color: black;
     margin-top: 50px;
    }

    </style>

     """,
    unsafe_allow_html=True
)


st.markdown("<h1> 🚀 Universal Unit Converter</h1>", unsafe_allow_html=True)

conversion_type = st.sidebar.selectbox("Select the conversion type", [
    "Length", "Mass", "Temperature", "Area", "Volume", "Time", "Speed", "Pressure", "Energy", "Frequency", 
    "Plane Angle", "Fuel Economy", "Data Transfer Rate", "Digital Storage", "Weight"
])

value = st.number_input("Enter the value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

unit_options = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
    "Mass": ["Kilograms", "Grams", "Pounds"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["Square Meters", "Square Kilometers", "Square Miles", "Hectares", "Acres"],
    "Volume": ["Liters", "Milliliters", "Cubic Meters"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"],
    "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour"],
    "Pressure": ["Pascals", "Bars", "Atmospheres"],
    "Energy": ["Joules", "Kilojoules", "Calories"],
    "Frequency": ["Hertz", "Kilohertz", "Megahertz"],
    "Plane Angle": ["Degrees", "Radians"],
    "Fuel Economy": ["Miles per gallon", "Kilometers per liter"],
    "Data Transfer Rate": ["Bits per second", "Kilobits per second"],
    "Digital Storage": ["Bytes", "Kilobytes", "Megabytes"],
    "Weight": ["Kilograms", "Grams", "Pounds"]
}

with col1:
    from_unit = st.selectbox("From", unit_options[conversion_type])
with col2:
    to_unit = st.selectbox("To", unit_options[conversion_type])

if st.button("🕹️ Convert"):
    result = convert_units(value, from_unit, to_unit, conversion_type)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Created with ❤️ by Anum Rajput</div>", unsafe_allow_html=True)