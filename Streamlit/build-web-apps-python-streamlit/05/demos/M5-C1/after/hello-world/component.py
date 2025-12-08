import streamlit.components.v1 as components


def hello_component(name):
    components.html(f"""<div style='font-size: 100px'
                             onclick='alert("Clicked!")'>
                        Hello {name}
                        </div>
""")


hello_component('world')
