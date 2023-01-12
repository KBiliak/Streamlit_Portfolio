import streamlit as st

def main_information():
    st.markdown('<div style="text-align: center; font-size: 50px;'
                'color: blue; text-align: center">Kateryna Biliak!</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: yellow;'>Python developer</h1>", unsafe_allow_html=True)
    st.text("Hello, my name is Kateryna and I am a junior Python Developer.\nI have an experience as a QA Engineer for one year.\n"
            "Now I am going to face with new chalanges like a development of interesting things")


def core_skills():
    st.markdown("<h2 style='text-align: center;'>Core skills</h2>", unsafe_allow_html=True)
    st.markdown(" - Solid knowledge in Programming fundamentals")
    st.markdown(" - Basic knowledge of HTTP (client-server architecture)")
    st.markdown(" - API, Postman understanding")
    st.markdown(" - Experience in Python server-side programming")
    st.markdown(" - Basic knowledge HTML/CSS/SQL")
    st.markdown(" - Organized, attentive, goal-oriented, analytical and communication skills")

def experience():
    st.markdown("<h2 style='text-align: center;'>Experience</h2>", unsafe_allow_html=True)
    st.markdown("<h4>Quality Assurance Engineer at Brights company</h4>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>(November 2021 - November 2022)</p>", unsafe_allow_html=True )

    st.markdown("Main Responsibilities:")
    st.markdown(" - Analyze and clarification of requirements with business analyst/manager")
    st.markdown(" - Create comprehensive and well-structured test plans and test cases")
    st.markdown(" - Conduct functional and regression testing")
    st.markdown(" - Perform thorough regression testing when bugs are resolved")
    st.markdown(" - Participate in the technical review process contributing behavioral viewpoint")


    st.markdown("<h2 style='text-align: center;'>Experience</h2>", unsafe_allow_html=True)
    st.markdown("<h4>Quality Assurance Engineer at Signum company</h4>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>(October  2021 - November 2021)</p>", unsafe_allow_html=True )
    st.markdown("Main Responsibilities:")
    st.markdown(" - Analyze actual results against the expected ones")
    st.markdown(" - Design test cases and sets of test cases to cover test conditions")
    st.markdown(" - Perform thorough regression testing")

def education():
    st.markdown("<h2 style='text-align: center;'>Education & certifications</h2>", unsafe_allow_html=True)
    st.text(" - National Technical University of Ukraine \'Kyiv Polytechnic Institute\nBachelor\'s degree, Linguistics\nSeptember 2015 - June 2019")
    st.text(" - Hillel IT School\nQA Manual \nJuly 2021 - November 2021")
    st.text(" - Udemy\nPython Developer in 2023: Zero to Mastery on 12/09/2022 as taught by Andrei Neagoie\n Novemver 2022 - Januar 2023")
    st.text(" - Udemy\nThe Python Mega Course: Learn Python in 40 Days with 20 Apps\nJanuar 2023 - till now")


def sidebar_information():
    st.sidebar.image("./img.jpg", width=240)

    image_location_container = st.sidebar.container()
    col1, col2 = st.sidebar.columns([1, 20])
    with image_location_container:
        with col1:
            st.image("./location.ico", width=20)
        with col2:
            st.markdown('<p style="color: white;">Toronto</p>',
                        unsafe_allow_html=True)

    contacts_container = st.sidebar.container()
    col1, col2 = st.sidebar.columns([1, 4])
    with contacts_container:
        with col1:
            st.text("Phone:\nE-mail:\nLinkedIn")
        with col2:
            st.markdown("<p>+1 289 894 1025\nkbiliak26@gmail.com\n<a href>linkedin.com/in/kateryna-biliak-011432217</a></p>",
                        unsafe_allow_html=True)


    st.sidebar.text_input("For more information write here", placeholder="For more information")


st.balloons()
main_information()
core_skills()
sidebar_information()
experience()
education()
