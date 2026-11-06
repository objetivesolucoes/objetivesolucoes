import streamlit as st
import streamlit.components.v1 as components

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Diagnóstico de Eficiência Comercial | Objetive",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização para remover as margens padrões do Streamlit e ocupar a tela inteira
st.markdown("""
    <style>
        .block-container { padding: 0px !important; }
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }
        header { visibility: hidden; }
    </style>
""", unsafe_index=True)

# Código HTML avançado fornecido pelo usuário
html_code = """
<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Diagnóstico de Eficiência Comercial | Objetive</title>
<script src="https://tailwindcss.com"></script>
<script src="https://jsdelivr.net"></script>
<style>:root{color-scheme:dark;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{background:#020617;color:#f1f5f9;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}</style>
</head><body>
<header class="border-b border-slate-800 bg-slate-900/60">
<div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
<img alt="Objetive Soluções Estratégicas" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAeAAAAC0CAMAAAB7Yg/yAAAAwFBMVEWq0OIHV9CfrtfS4/JwpN9rs7Uqd7VjZLF/f3+9vb97+PwAM8sEJ6BgfM4AP38A/wC5/7n//7IASMDo7PgAVVU5rOX/f///v79//3//AAD/f3///38AAAD+/v7+/v4AR733+fz6+/3+/v79/f78/P39/f4AAP8Af38AVaoA//8Af//o6ffT2PYAScHV5vUBSLgAPr4AR720//+7vvsAR70AR7wAR70AR71/f/8AR70AAH+qqv/n7PeqqqrMzMxqms/JV12qAAAAQHRSTlMIDQcIBgMEAwIEAgUECAQBAwNJRAMEAgQCAQICAP0E9jBP0K9vkAECAwECEQ3+Fg8FzwMFsS+PbgJQAgMtAwUFbaGwWQAAJsxJREFUeNrtfQl72zqutrwnac8yM/feb6NxtC+2ajt20rpxlv//rz6CpCRu2myndVrzmelpE4kC8RIkCICAQ67tl27OlQUfrcW0XQH+ZdFdiP8mi3RBW/oUPz09xbxdAf7ILSMk2Xymf1kPBoO05qFFStuCtSRJ0yvAH6gtSPr5M1l/e7i/f3h4+Erbt2/fv//7+yNtg/V6nQ4GoL0y2FwB/kBtMI3J48M//3z55x/5D2z32B447gg7bY8DCnt6BfgDtXRM1l9LTM325Qv+X3rgfkCSK8AfB98BSb814Gtp3+m6fgX4o7T1mqwfeuH7z+MV4I8kwWvy+M8V4F+3fV6T770Bvu7BHwrgnlvwFeAP1Ta9AaZa9NMV4A+kZfUGeE3iK8AfSIShp5J1v7kC/IHaE/m0eeglwg+DK8AfqMWblKrRfRB+uC7RH0uNHmSDb30QfkDX4hXgj6VofbtHe/OXTjB/pcv6FeCPhW9K1t+/oasQXUcPzIl03wDw4grwB9uH08GsOhcPBoM1/ePxkf7v+7+/f//+VQf46i78YG02IAt1uqG4AnfuFxE8vD1eAf4oLf2UAiQJ/VtGW3VU2hRxV8kiiQn+I92kCQbqLNbrmWar/nZdoi+2ZYuYhU9mCbaOGzQxAE6uAF/wbpsOBul6gFF0Tx0B/mb6+68AX2bDcDkN8WRBV2K2GD/xQFn9ialuq74CfKnSS___6RED52hbY8Bk3U69eML9d8M0rZsp+XoF+AO0p+SPlAy+yQGTRbhkFSe7HqzTUoEeC7SJacobHwF4EtcnhcYfKUI4xcWNPlFD5P9KmAfMIAT8qD7+68AX2DbfErJ11ZTJKLNbZZfvtwzUY3J5grwh1iiN3Ffv++abds3G81qub4CfJlLdAcBtgEcDxSAv9xfAb5MGwdJ+4U/f3nYcN17rQOMsF8BvrxD0vq+3xL9MOPvDVTc75nudQX48gB+7Atw8Z4m2O8FMMAldXPiB96dinNIcA3As/cAGJAjAKfyhb0P78jdgs76J5JYDONHY7xY94ut++crdytpvoYvD2RzfoD/xi6dTydyBd8d5zvxt3fBl/5/tUoJean9QpqOcDCr4Q+G+NNm8bWfksVCcyia3/Qfr88NMEyIG/nzuR+5J2CD7PQC2k0QwvSghiOMDof3t7f3tN58icEE3vdNOE9X6ymzViLM0I5sYQZw4hwOlH3lULDs9PkZiBsU2XTvyVpKmVt8IKyTS/ihtPGhd4J40EsEmWOfrtNfdYDPvUTDtgSGTuwfizDFfcToG/gXWytBV08nkEgiy/2BCMcDGDz800OImdeINs0+cnaAVWSOhgZW_lxjbnJnfF6fTtO5elAH4zs3QOIfBXFHBt8fTLNzXbTsN8agGDSJ5oJ9VoADhSfHrWsa+xn_k_cTYNoonSbAqgDzfSH_cUKcks368RF9wugtYoGyX2sDZR85gwYPNsE_H8B0qfN1xp2_DsyDdwBYmYi4RtgAVgcT_lCAyWdPQDY21f7TYLNeG16jJ9yC0_cGmMBcZ9wZ5Os9APZ14bQliV9bgEl_vGzSdm0wNmvK6p7O_m_wHqZp6NiaLxRgE5D1EwDWN2rvggDW_9U_Un4CwNo56fliBJiiqAPMA+MH2s_X4pW_Yk4FGAWwU8F+mb9wVwHwB4fT6fA_vX_0gB_0Zq8A74g8fFw8wA0Ad_FwNTheiW7wWQDf4f0R9A_f1oQnlW4AeOwA9_t32pT72gBupunWf31_2YMB3_o6D_f7_VwVbA9gS7t47WB_uEyx3p0MYFYm_gSwn5v6HkPDKA8m3w_wqK_A4rWkAL_A6nSTAL_AtW_A_onE6t_uEoaA+0CAnW36N8XJ6mZ7sDIUoasBDoIDf9u7P1t5CDB2_P2gEWB_gW8GfBwVwIscTrLQ051RgDtIcEL_djfL
