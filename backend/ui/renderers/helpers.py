import streamlit as st


# ---------------------------------------------------
# EDIT MODE
# ---------------------------------------------------

def is_edit_mode():
    return st.session_state.get("edit_mode", False)


# ---------------------------------------------------
# SECTION HEADINGS
# ---------------------------------------------------

def section_heading(title):
    st.markdown(
        f"""
        <div style="
            padding:16px 20px;
            margin:24px 0 18px 0;
            background:#F8FAFC;
            border:1px solid #E2E8F0;
            border-left:5px solid #2563EB;
            border-radius:12px;
        ">
            <div style="
                font-size:22px;
                font-weight:700;
                color:#0F172A;
            ">
                {title}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def sub_heading(title):
    st.markdown(
        f"""
<div style="
padding:8px 14px;
margin-top:15px;
margin-bottom:10px;
background:#F8FAFC;
border-radius:8px;
font-size:18px;
font-weight:600;
color:#334155;
">
{title}
</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------
# TEXT
# ---------------------------------------------------

def render_text(obj, field, label, key):

    value = obj.get(field, "")

    if is_edit_mode():

        obj[field] = st.text_input(
            label,
            value,
            key=key,
        )

    else:

        st.markdown(
            f"""
<div style="margin-bottom:12px;">
<div style="
font-size:13px;
font-weight:600;
color:#64748B;
text-transform:uppercase;
letter-spacing:.5px;
">{label}</div>

<div style="
font-size:16px;
padding-top:2px;
">
{value if value else "<span style='color:#94A3B8;'>Not provided</span>"}
</div>
</div>
""",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------
# TEXT AREA
# ---------------------------------------------------

def render_textarea(obj, field, label, key, height=120):

    value = obj.get(field, "")

    if is_edit_mode():

        obj[field] = st.text_area(
            label,
            value,
            height=height,
            key=key,
        )

    else:

        st.markdown(
            f"""
<div style="margin-bottom:16px;">
<div style="
font-size:13px;
font-weight:600;
color:#64748B;
text-transform:uppercase;
letter-spacing:.5px;
">{label}</div>

<div style="
background:#F8FAFC;
padding:15px;
border-radius:10px;
border:1px solid #E2E8F0;
margin-top:5px;
line-height:1.6;
">
{value if value else "<span style='color:#94A3B8;'>No information provided.</span>"}
</div>
</div>
""",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------
# NUMBER
# ---------------------------------------------------

def render_number(obj, field, label, key):

    value = obj.get(field, 0)

    if is_edit_mode():

        obj[field] = st.number_input(
            label,
            value=int(value),
            key=key,
        )

    else:

        render_text(obj, field, label, key)


# ---------------------------------------------------
# LIST
# ---------------------------------------------------

def render_list(obj, field, label, key):

    values = obj.get(field, [])

    if values is None:
        values = []

    # -----------------------------
    # FIX STRING BUG
    # -----------------------------

    if isinstance(values, str):

        values = [
            line.strip()
            for line in values.split("\n")
            if line.strip()
        ]

    if is_edit_mode():

        text = "\n".join(values)

        updated = st.text_area(
            label,
            text,
            height=140,
            key=key,
        )

        obj[field] = [
            line.strip()
            for line in updated.split("\n")
            if line.strip()
        ]

    else:

        st.markdown(
            f"""
<div style="
font-size:13px;
font-weight:600;
color:#64748B;
text-transform:uppercase;
letter-spacing:.5px;
margin-bottom:8px;
">
{label}
</div>
""",
            unsafe_allow_html=True,
        )

        if len(values) == 0:

            st.info("No information available.")

        else:

           for item in values:
                st.markdown(
                    f"""
                    <div style="
                        background:white;
                        border:1px solid #E2E8F0;
                        border-radius:10px;
                        padding:12px 16px;
                        margin-bottom:10px;
                        box-shadow:0 2px 8px rgba(0,0,0,.03);
                    ">
                        {item}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# ---------------------------------------------------
# STATUS
# ---------------------------------------------------

def render_status():

    if st.session_state.get("approved", False):
        st.success("Approved")

    elif st.session_state.get("edit_mode", False):
        st.warning("Editing")

    else:
        st.info("Draft")


# ---------------------------------------------------
# DIVIDER
# ---------------------------------------------------

def divider():

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()