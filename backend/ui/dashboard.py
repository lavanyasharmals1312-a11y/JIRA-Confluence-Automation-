import streamlit as st


def show_dashboard():

    # =====================================================
    # HERO
    # =====================================================

    st.markdown(
        """
        <div style="
        background:linear-gradient(135deg,#2563EB,#4F46E5);
        padding:35px;
        border-radius:22px;
        color:white;
        margin-bottom:25px;
        box-shadow:0 12px 30px rgba(37,99,235,.25);
        ">

        <div style="
        font-size:38px;
        font-weight:800;
        margin-bottom:8px;
        ">
        AI Requirements Intelligence Platform
        </div>

        <div style="
        font-size:18px;
        opacity:.92;
        ">
        Generate enterprise-ready Jira backlogs from Business Requirement Documents using AI.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # KPI
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Projects",
            "12",
            "+3"
        )

    with c2:

        st.metric(
            "Backlogs",
            "27",
            "+5"
        )

    with c3:

        st.metric(
            "Requirements",
            "84",
            "+12"
        )

    with c4:

        st.metric(
            "⚙ Integrations",
            "2"
        )

    st.write("")

    # =====================================================
    # QUICK OVERVIEW
    # =====================================================

    left, right = st.columns([2, 1])

    with left:

        st.markdown("## Platform Overview")

        st.info(
            """
The platform converts Business Requirement Documents into a structured Jira backlog.

✔ Executive Summary

✔ Epics

✔ Features

✔ User Stories

✔ Tasks

✔ Jira Publishing

✔ PDF Export
"""
        )

    with right:

        st.markdown("## AI Configuration")

        st.success(
            """
**Provider**

Gemini 2.5 Flash

---

**Output**

Jira Ready JSON

---

**Status**

Ready
"""
        )

    st.divider()

    # =====================================================
    # PIPELINE
    # =====================================================

    st.markdown("# Workflow")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:

        st.success(
            """
### 

Upload BRD

✔
"""
        )

    with c2:

        st.success(
            """
###

Generate

✔
"""
        )

    with c3:

        st.info(
            """
###

Review

Pending
"""
        )

    with c4:

        st.info(
            """
###

Approve

Pending
"""
        )

    with c5:

        st.info(
            """
### 

Publish

Pending
"""
        )

    st.divider()

    # =====================================================
    # RECENT PROJECTS
    # =====================================================

    st.markdown("# Recent Projects")

    projects = [

        {
            "Project": "Banking Portal",
            "Status": "Generated",
            "Owner": "Business Team",
            "Updated": "Today",
        },

        {
            "Project": "Healthcare Platform",
            "Status": "Approved",
            "Owner": "HR Team",
            "Updated": "Yesterday",
        },

        {
            "Project": "Employee Leave System",
            "Status": "Published",
            "Owner": "IT",
            "Updated": "2 Days Ago",
        },

        {
            "Project": "CRM Modernization",
            "Status": "Draft",
            "Owner": "Sales",
            "Updated": "4 Days Ago",
        },

    ]

    cols = st.columns(2)

    for i, project in enumerate(projects):

        with cols[i % 2]:

            st.markdown(
                f"""
<div style="
background:white;
padding:22px;
border-radius:18px;
border:1px solid #E5E7EB;
box-shadow:0 6px 20px rgba(0,0,0,.05);
margin-bottom:18px;
">

<div style="
font-size:22px;
font-weight:700;
margin-bottom:10px;
">

{project["Project"]}

</div>

<div style="font-size:15px;">

<b>Status</b><br>
{project["Status"]}

<br><br>

<b>Owner</b><br>
{project["Owner"]}

<br><br>

<b>Last Updated</b><br>
{project["Updated"]}

</div>

</div>
""",
                unsafe_allow_html=True,
            )

    st.divider()

    # =====================================================
    # PLATFORM FEATURES
    # =====================================================

    st.markdown("# Platform Capabilities")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.success(
            """
### Document Intelligence

• PDF Parsing

• Requirement Extraction

• AI Analysis
"""
        )

    with c2:

        st.success(
            """
### Backlog Generation

• Epics

• Features

• User Stories

• Tasks
"""
        )

    with c3:

        st.success(
            """
### Delivery

• Jira Integration

• PDF Export

• Project History
"""
        )