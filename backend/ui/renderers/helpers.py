import streamlit as st


# ---------------------------------------------------
# READ / EDIT MODE
# ---------------------------------------------------

def is_edit_mode():

    return st.session_state.get(
        "edit_mode",
        False
    )


# ---------------------------------------------------
# SECTION HEADINGS
# ---------------------------------------------------

def section_heading(title):

    st.markdown(f"## {title}")


def sub_heading(title):

    st.markdown(f"### {title}")


# ---------------------------------------------------
# TEXT
# ---------------------------------------------------

def render_text(

    obj,

    field,

    label,

    key

):

    value = obj.get(field, "")

    if is_edit_mode():

        obj[field] = st.text_input(

            label,

            value,

            key=key

        )

    else:

        st.markdown(f"**{label}**")

        st.write(value)


# ---------------------------------------------------
# TEXT AREA
# ---------------------------------------------------

def render_textarea(

    obj,

    field,

    label,

    key,

    height=120

):

    value = obj.get(field, "")

    if is_edit_mode():

        obj[field] = st.text_area(

            label,

            value,

            height=height,

            key=key

        )

    else:

        st.markdown(f"**{label}**")

        st.write(value)


# ---------------------------------------------------
# NUMBER
# ---------------------------------------------------

def render_number(

    obj,

    field,

    label,

    key

):

    value = obj.get(field, 0)

    if is_edit_mode():

        obj[field] = st.number_input(

            label,

            value=int(value),

            key=key

        )

    else:

        st.markdown(f"**{label}**")

        st.write(value)


# ---------------------------------------------------
# LIST
# ---------------------------------------------------

def render_list(

    obj,

    field,

    label,

    key

):

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

        st.markdown(f"**{label}**")

        if len(values) == 0:

            st.caption("None")

        else:

            for item in values:

                st.markdown(f"- {item}")


# ---------------------------------------------------
# STATUS BADGE
# ---------------------------------------------------

def render_status():

    if st.session_state.get(

        "approved",

        False

    ):

        st.success(

            "Status : Approved"

        )

    elif st.session_state.get(

        "edit_mode",

        False

    ):

        st.warning(

            "Status : Editing"

        )

    else:

        st.info(

            "Status : Draft"

        )


# ---------------------------------------------------
# DIVIDER
# ---------------------------------------------------

def divider():

    st.divider()