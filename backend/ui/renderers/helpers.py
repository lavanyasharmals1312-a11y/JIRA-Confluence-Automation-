import html
import streamlit as st


# ---------------------------------------------------
# READ / EDIT MODE
# ---------------------------------------------------

def is_edit_mode():
    return st.session_state.get("edit_mode", False)


# ---------------------------------------------------
# SECTION HEADINGS
# ---------------------------------------------------

def section_heading(title):

    st.markdown(
        f"""
<h3 style="
margin-top:10px;
margin-bottom:10px;
font-size:28px;
font-weight:700;
">
{html.escape(str(title))}
</h3>
""",
        unsafe_allow_html=True,
    )


def sub_heading(title):
    st.markdown(f"### {html.escape(str(title))}")


# ---------------------------------------------------
# TEXT
# ---------------------------------------------------

def render_text(obj, field, label, key):

    raw_value = obj.get(field, "")

    if is_edit_mode():

        obj[field] = st.text_input(
            label,
            raw_value,
            key=key
        )

    else:

        value = html.escape(str(raw_value))

        st.markdown(
            f"""
<div style="margin-bottom:10px;">
    <div style="font-weight:600;font-size:15px;">
        {html.escape(label)}
    </div>
    <div style="font-size:15px;margin-top:2px;">
        {value}
    </div>
</div>
""",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------
# TEXT AREA
# ---------------------------------------------------

def render_textarea(obj, field, label, key, height=120):

    raw_value = obj.get(field, "")

    if is_edit_mode():

        obj[field] = st.text_area(
            label,
            raw_value,
            height=height,
            key=key
        )

    else:

        value = html.escape(str(raw_value)).replace("\n", "<br>")

        st.markdown(
            f"""
<div style="margin-bottom:10px;">
    <div style="font-weight:600;font-size:15px;">
        {html.escape(label)}
    </div>
    <div style="font-size:15px;margin-top:2px;line-height:1.5;">
        {value}
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
            key=key
        )

    else:

        st.markdown(
            f"""
<div style="margin-bottom:10px;">
    <div style="font-weight:600;font-size:15px;">
        {html.escape(label)}
    </div>
    <div style="font-size:15px;margin-top:2px;">
        {value}
    </div>
</div>
""",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------
# LIST
# ---------------------------------------------------

def render_list(obj, field, label, key):

    values = obj.get(field, [])

    if values is None:
        values = []

    if is_edit_mode():

        text = "\n".join(values)

        updated = st.text_area(
            label,
            text,
            height=130,
            key=key
        )

        obj[field] = [
            line.strip()
            for line in updated.split("\n")
            if line.strip()
        ]

    else:

        st.markdown(f"**{html.escape(label)}**")

        if not values:

            st.caption("None")

        else:

            bullet_html = """
<ul style="
padding-left:20px;
margin-top:4px;
margin-bottom:6px;
line-height:1.4;
">
"""

            for item in values:
                bullet_html += f"""
<li style="
white-space:normal;
word-break:normal;
overflow-wrap:break-word;
margin-bottom:4px;
">
{html.escape(str(item))}
</li>
"""

            bullet_html += "</ul>"

            st.markdown(
                bullet_html,
                unsafe_allow_html=True
            )


# ---------------------------------------------------
# STATUS BADGE
# ---------------------------------------------------

def render_status():

    if st.session_state.get("approved", False):

        st.success("Status : Approved")

    elif st.session_state.get("edit_mode", False):

        st.warning("Status : Editing")

    else:

        st.info("Status : Draft")


# ---------------------------------------------------
# DIVIDER
# ---------------------------------------------------

def divider():

    st.markdown("<div style='margin:10px 0'></div>", unsafe_allow_html=True)
    st.divider()