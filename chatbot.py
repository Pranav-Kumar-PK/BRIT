import streamlit as st
import gettext
import os
import base64
import lang_map
lang_dict = lang_map.lang_dict
FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))
# _ = gettext.gettext

st.image('Britannia_Industries_logo.png', width=400)

print(lang_dict)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        # background-color: red;
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# set_background('Britannia_Industries_logo1.png')


col1, col2, col3 = st.columns(3)

with col3:
    language = st.selectbox('', ['English', 'Hindi', 'Kannada'])
    st.text("")
    st.text("")

try:
    localizator = gettext.translation(
        'guess', localedir='locales', languages=[lang_dict[language]])
    localizator.install()
#   _ = localizator.gettext
except:
    pass

# hi = gettext.translation('guess', localedir=os.path.join(FOLDER_OF_THIS_FILE, 'locales'), languages=['hi'])
# hi.install()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")

st.markdown("""# B.R.I.T.""")

st.write(_("Hi there! Did you recently experience a sudden decline in your purchase rate from Britannia?"))
res1 = st.text_input(_('Please select'),
                     placeholder='Yes or No', key='ujytr86')
res1 = res1.lower()

problems_arr = []

if res1 == 'no':
    st.write(_('Thanks for your time!'))
if res1 == 'yes':
    st.text("")
    st.text(
        _("What are the possible reasons for the sudden change and caused inconvenience"))

    res2 = st.multiselect(_('you can select multiple options'),
                          [
                              _('Replaced a premium Britannia product with less premium Britannia product'),
                              _('Stopped selling that category'),
                              _('Started selling products of competition brand'),
                              _('Less demand of the category in the market')
    ], key='uyjf764td')
    problems_arr.extend(res2)
    res3 = ''
    if st.checkbox(_('Other'), value=False, key='jkyt87i'):
        res3 = st.text_area(_('State your reason'), key='jydi864i')
    problems_arr.extend(res3)
    st.text("")
    if "submit_button1" not in st.session_state:
        st.session_state.submit_button1 = False

    if st.button(_('Submit'), key='87ifkh') or st.session_state.submit_button1:
        st.session_state.submit_button1 = True
        st.write(
            _('Thank You for your response, we would now proceed to the next segment'))
        st.text("")
        st.text("")
        if st.checkbox(_('Proceed to the next segment'), value=False, key='jy477jv'):

            st.text("")
            res2 = st.multiselect(_('Select multiple options'),
                                  [
                                      _('Payments due from Britannia'),
                                      _('Received poor quality products'),
                                      _('Refund related issues'),
                                      _('Products not delivered on-time'),
                                      _('Received damaged products'),
                                      _('Irregular visits from salesperson'),
                                      _('Shipment not delivered')
            ], key="xHrtdg7")
            problems_arr.extend(res2)
            res3 = ''
            if st.checkbox(_('Other'), value=False, key='32dtfj'):
                res3 = st.text_area(_('State your reason'), key='jhvtsui')
            problems_arr.extend(res3)

            st.text("")

            if "submit_button2" not in st.session_state:
                st.session_state.submit_button2 = False

            if st.button(_('Submit'), key='87ikht') or st.session_state.submit_button2:
                st.session_state.submit_button2 = True
                st.write(
                    _('Thank You for your response, we would now proceed to the next segment'))
                st.text("")
                st.text("")
                if st.checkbox(_('Proceed to the next section'), value=False, key='htdu57'):

                    st.text("")
                    res2 = st.multiselect(_('Select multiple options'),
                                          [
                                              _('Average price/kg reduced'),
                                              _('Buying less number of packets'),
                                              _('Schemes are not available')
                    ], key="ujtd86")
                    problems_arr.extend(res2)
                    res3 = ''
                    if st.checkbox(_('Other'), value=False, key='kjchi758'):
                        res3 = st.text_area(
                            _('State your reason'), key='jtdu47')
                    problems_arr.extend(res3)

                    st.text("")

                    if "submit_button3" not in st.session_state:
                        st.session_state.submit_button3 = False

                    if st.button(_('Submit'), key='jhc85') or st.session_state.submit_button3:
                        st.session_state.submit_button3 = True
                        st.write(
                            _('We have recorded your response. Would you like to add any other issue you are facing and help us in getting better?'))
                        res4 = st.radio(
                            _('Select'), [_('Yes'), _('No')], index=0)
                        if res4 == 'Yes':
                            st.text_area(_('State your issue'), key='iaug923y')

                        if "submit_button4" not in st.session_state:
                            st.session_state.submit_button4 = False

                        if st.button(_('Submit'), key='khv658') or st.session_state.submit_button4:
                            st.session_state.submit_button4 = True
                            st.text('')
                            st.header(
                                _('These are the issues you are facing currently:'))
                            st.markdown(
                                _("""##### Can you select the degree of severity of these problems"""))
                            st.text('')
                            # st.write(problems_arr)
                            for prob in problems_arr:
                                st.radio(
                                    prob, [_('Low'), _('Medium'), _('High')])

                            if "submit_button5" not in st.session_state:
                                st.session_state.submit_button5 = False

                            if st.button(_('Submit'), key='kjdb9326') or st.session_state.submit_button5:
                                st.session_state.submit_button5 = True
                                st.write(_('Thank you for your response!'))

elif res1 != '':
    st.write(_('Please type YES or NO'))
