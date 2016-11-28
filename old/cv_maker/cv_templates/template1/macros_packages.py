macros_packages = r"""
\documentclass[paper=a4,fontsize=11pt]{scrartcl}
\usepackage[brazil]{babel}
\usepackage[utf8x]{inputenc}
\usepackage[protrusion=true,expansion=true]{microtype}
\usepackage{amsmath,amsfonts,amsthm}
\usepackage{graphicx}
\usepackage[svgnames]{xcolor}
\usepackage{geometry}
    \textheight=700px
\usepackage{url}
\frenchspacing
\pagestyle{empty}
\usepackage{sectsty}
\sectionfont{
    \usefont{OT1}{phv}{b}{n}
    \sectionrule{0pt}{0pt}{-5pt}{3pt}}

\newlength{\spacebox}
\settowidth{\spacebox}{8888888888}
\newcommand{\sepspace}{\vspace*{1em}}

\newcommand{\MyName}[1]{
        \Huge \usefont{OT1}{phv}{b}{n} \hfill #1
        \par \normalsize \normalfont}

\newcommand{\MySlogan}[1]{
        \large \usefont{OT1}{phv}{m}{n}\hfill \textit{#1}
        \par \normalsize \normalfont}

\newcommand{\NewPart}[1]{\section*{\uppercase{#1}}}

\newcommand{\PersonalEntry}[2]{
        \noindent\hangindent=2em\hangafter=0
        \parbox{\spacebox}{
        \textit{#1}}
        \hspace{1.5em} #2 \par}

\newcommand{\SkillsEntry}[2]{
        \noindent\hangindent=2em\hangafter=0
        \parbox{\spacebox}{
        \textit{#1}}
        \hspace{1.5em} #2 \par}

\newcommand{\EducationEntry}[4]{
        \noindent \textbf{#1} \hfill
        \colorbox{Black}{%
            \parbox{6em}{%
            \hfill\color{White}#2}} \par
        \noindent \textit{#3} \par
        \noindent\hangindent=2em\hangafter=0 \small #4
        \normalsize \par}

\newcommand{\WorkEntry}[4]{
        \noindent \textbf{#1} \hfill
        \colorbox{Black}{\color{White}#2} \par
        \noindent \textit{#3} \par
        \noindent\hangindent=2em\hangafter=0 \small #4
        \normalsize \par}

\begin{document}

\MyName{(%(name))}
\MySlogan{(%(slogan))}
"""
