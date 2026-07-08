import streamlit as st
import streamlit.components.v1 as components
from groq import Groq
import base64

# ---- API ----
client = Groq(api_key=st.secrets["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"])

# ---- KNOWLEDGE BASE ----
COLLEGE_INFO = """
JSS UNIVERSITY NOIDA - COMPLETE INFORMATION

ABOUT:
- Full name: JSS University, Noida (formerly JSSATE)
- Established: 1998, University status in 2024
- Campus: 28-acre green campus in Sector 62 Noida
- Approved by: AICTE, UGC
- Ranking: #201-300 in Engineering nationally
- QS I-GAUGE Gold College Rating
- 4.5 Star by Ministry of Education Innovation Cell
- Total students: 4000+, Alumni: 18,000+

CONTACT:
- Website: jssuninoida.edu.in
- Email: admissions@jssuninoida.edu.in
- Phone: +91-9311830458
- Address: C-20/1, Sector-62, Noida, UP-201301

UNDERGRADUATE PROGRAMS (BTech 4 years):
- CSE (Computer Science Engineering)
- CSE-DS (Data Science)
- CSE-AI/ML
- ECE (Electronics & Communication)
- Mechanical Engineering
- Civil Engineering
- B.Pharma (Pharmacy)
- BCA, B.Sc

POSTGRADUATE PROGRAMS:
- MBA (2 years)
- MCA (2 years)
- M.Tech (2 years)
- PhD (3 years)

FEES:
- BTech: 1-2 lakh per year (approx 2.6L/yr)
- Hostel: 98,000 to 1,34,000 per year (mess included)
- Registration Fee: Rs 2,000
- Security Deposit: Rs 10,000 (refundable)
- Exam Fee: Rs 7,500 per year
- MBA: 1.33 lakh per year
- MCA: 1.22-1.95 lakh total
- M.Tech: 1.28 lakh total

ADMISSIONS:
- BTech: 85% seats via JEE Main/UPCET scores
- Remaining 15%: direct via AKTU counselling
- Eligibility: 10+2 with PCM min 45% marks
- MBA: CUET score or 60% in graduation
- Apply at jssuninoida.edu.in
- No reservation - purely merit based
- Hostel: first-come first-served basis

PLACEMENTS:
- Overall placement rate: 80%
- CSE placement rate: 87%
- Students placed in 2025: 600+
- Highest package: 47 LPA
- Average package: 5-6 LPA
- Top recruiters: TCS, Wipro, Amazon, Samsung,
  Tech Mahindra, Nagarro, Capgemini, JP Morgan,
  HP India, Cognizant, Infosys, HCL, Byju's,
  Torrent Power, KEC, Hashedin

HOSTEL:
- Separate boys and girls hostels
- Boys capacity: 540, Girls capacity: 700
- AC and Non-AC options available
- Mess/dining facility included
- 24/7 security

CAMPUS FACILITIES:
- Modern computer and research labs
- Digital library
- Sports: Cricket, Football, Basketball,
  Badminton, Table Tennis, Athletics
- Gymnasium and sports grounds
- Primary Health Centre
- Student Activity Centre
- JSS STEP Startup Incubation Park
- Coding, Robotics, Soft skills labs

SCHOLARSHIPS:
- AICTE PM Special Scholarship (J&K/Uttarakhand)
- NSP Minority Scholarship
- AICTE Pragati & Saksham schemes
- UP Govt scholarships (SC/ST/OBC/EWS)
- Merit fee concessions for JEE toppers
- Contact accounts section for details

NOTABLE ALUMNI:
- Anuj Swarup (ECE 2006) - IFS Officer
- Harsh Singh (IT 2009) - IAS Officer
- Saurabh Pandey (ECE 2002) - Govt of Australia
- Akshat Bhatnagar (ECE 2004) - Samsung

ANNUAL EVENTS:
- Zealicon - Major annual college fest
- Technical and cultural events year round
"""

# ---- LOAD IMAGES ----
def load_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

campus_b64 = load_image_base64("campus.jpeg")
logo_b64 = load_image_base64("logo.jpeg")

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="JSS University Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ---- BACKGROUND ----
if campus_b64:
    bg_css = f"""
    .stApp {{
        background-image: url("data:image/jpeg;base64,{campus_b64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    """
else:
    bg_css = """
    .stApp {
        background: linear-gradient(135deg, #0a1e50, #1e3a8a);
    }
    """

# ---- ALL CSS ----
st.markdown(f"""
<style>
{bg_css}

.stApp::before {{
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(5, 20, 60, 0.80);
    z-index: 0;
}}

/* Hide streamlit elements */
footer {{ display: none !important; }}
#MainMenu {{ display: none !important; }}
header {{ display: none !important; }}
.stDeployButton {{ display: none !important; }}

/* All content above overlay */
.block-container {{
    position: relative;
    z-index: 1;
    padding-top: 20px !important;
}}

/* Header */
.main-header {{
    display: flex;
    align-items: center;
    gap: 15px;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
    padding: 14px 20px;
    border-radius: 16px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.25);
}}
.header-text h1 {{
    color: white !important;
    margin: 0;
    font-size: 24px;
    font-weight: bold;
    font-family: Arial;
}}
.header-text p {{
    color: #93C5FD;
    margin: 3px 0 0 0;
    font-size: 13px;
    font-family: Arial;
}}

/* Quick buttons */
.stButton > button {{
    background: rgba(255,255,255,0.18) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.4) !important;
    border-radius: 20px !important;
    font-size: 13px !important;
    font-weight: bold !important;
    padding: 6px 14px !important;
    width: 100% !important;
    backdrop-filter: blur(5px);
    transition: all 0.2s;
}}
.stButton > button:hover {{
    background: rgba(255,255,255,0.35) !important;
    transform: scale(1.03);
}}

/* Input box */
.stChatInput > div {{
    background: rgba(255,255,255,0.95) !important;
    border-radius: 25px !important;
    border: 2px solid #3B82F6 !important;
}}

/* Spinner */
.stSpinner > div {{
    border-color: white !important;
}}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
if logo_b64:
    logo_html = f'<img src="data:image/jpeg;base64,{logo_b64}" width="58" style="border-radius:10px;">'
else:
    logo_html = '<div style="font-size:42px">🎓</div>'

st.markdown(f"""
<div class="main-header">
    {logo_html}
    <div class="header-text">
        <h1>JSS University, Noida</h1>
        <p>🟢 Online &bull; Official 24/7 AI Assistant</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- QUICK BUTTONS ----
col1, col2, col3, col4 = st.columns(4)
quick_q = None
with col1:
    if st.button("💰 Fees"): quick_q = "What are the BTech fees?"
with col2:
    if st.button("🎯 Placements"): quick_q = "Tell me about placements and packages"
with col3:
    if st.button("📝 Admissions"): quick_q = "How to apply for BTech admission?"
with col4:
    if st.button("🏠 Hostel"): quick_q = "Tell me about hostel facilities and fees"

st.markdown("<div style='margin-bottom:10px'></div>", unsafe_allow_html=True)

# ---- CHAT HISTORY ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",
            "content": f"""You are the official AI assistant for JSS University Noida.
STRICT RULES:
1. ONLY answer using the KNOWLEDGE BASE below
2. Never make up information
3. Keep answers SHORT and clear - max 4 lines
4. If info not in knowledge base say:
   "For accurate info contact: admissions@jssuninoida.edu.in or +91-9311830458"
5. Refuse non-college questions politely
6. Be warm, friendly and professional

KNOWLEDGE BASE:
{COLLEGE_INFO}"""
        }
    ]

# ---- BUILD CHAT HTML ----
def build_chat_html(messages, campus_b64):
    bg = f'background-image: url("data:image/jpeg;base64,{campus_b64}"); background-size: cover;' if campus_b64 else 'background: rgba(255,255,255,0.05);'

    html = f"""
    <html>
    <head>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: Arial, sans-serif; }}
        body {{
            {bg}
            background-color: #0a1e50;
            padding: 15px;
            min-height: 400px;
        }}
        body::before {{
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(5, 20, 60, 0.80);
            z-index: 0;
        }}
        .chat-wrap {{
            position: relative;
            z-index: 1;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        /* USER - RIGHT */
        .user-row {{
            display: flex;
            justify-content: flex-end;
        }}
        .user-bubble {{
            background: linear-gradient(135deg, #1E3A8A, #3B82F6);
            color: white;
            padding: 10px 14px;
            border-radius: 18px 18px 3px 18px;
            max-width: 70%;
            font-size: 14px;
            line-height: 1.5;
            box-shadow: 0 2px 8px rgba(0,0,0,0.4);
            word-wrap: break-word;
        }}

        /* BOT - LEFT */
        .bot-row {{
            display: flex;
            justify-content: flex-start;
            align-items: flex-end;
            gap: 8px;
        }}
        .bot-avatar {{
            background: #1E3A8A;
            color: white;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 17px;
            flex-shrink: 0;
            border: 2px solid #93C5FD;
        }}
        .bot-bubble {{
            background: white;
            color: #111;
            padding: 10px 14px;
            border-radius: 18px 18px 18px 3px;
            max-width: 70%;
            font-size: 14px;
            line-height: 1.5;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            word-wrap: break-word;
        }}
    </style>
    </head>
    <body>
    <div class="chat-wrap">
    """

    # Welcome message
    if len(messages) == 1:
        html += """
        <div class="bot-row">
            <div class="bot-avatar">🎓</div>
            <div class="bot-bubble">
                👋 <b>Welcome to JSS University Noida!</b><br>
                I can help with admissions, fees, courses,
                placements, hostel and more!<br>
                What would you like to know? 😊
            </div>
        </div>
        """

    for msg in messages[1:]:
        if msg["role"] == "user":
            html += f"""
            <div class="user-row">
                <div class="user-bubble">{msg['content']}</div>
            </div>
            """
        else:
            content = msg['content'].replace('\n', '<br>')
            html += f"""
            <div class="bot-row">
                <div class="bot-avatar">🎓</div>
                <div class="bot-bubble">{content}</div>
            </div>
            """

    html += """
    </div>
    <script>window.scrollTo(0, document.body.scrollHeight);</script>
    </body></html>
    """
    return html

# ---- DISPLAY CHAT ----
chat_html = build_chat_html(st.session_state.chat_history, campus_b64)
components.html(chat_html, height=420, scrolling=True)

# ---- INPUT ----
user_input = st.chat_input("Ask about admissions, fees, placements...")

if quick_q:
    user_input = quick_q

if user_input:
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )

    # Token saving - only last 6 messages
    recent = [st.session_state.chat_history[0]] + \
             st.session_state.chat_history[-6:]

    with st.spinner(""):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=recent,
            max_tokens=300,
            temperature=0.3
        )
    reply = response.choices[0].message.content

    st.session_state.chat_history.append(
        {"role": "assistant", "content": reply}
    )
    st.rerun()
