import atlastk
 
BODY = """
<fieldset>
 <input id="Input" data-xdh-onevent="Submit" value="World"/>
 <button data-xdh-onevent="Submit">Hello</button>
 <hr/>
 <fieldset>
  <output id="Output">Greetings displayed here!</output>
 </fieldset>
</fieldset>
"""
 
def ac_connect(dom):
  dom.inner("", BODY)
  dom.focus("Input")
 
def ac_submit(dom):
  global name
  name = dom.get_value("Input")
  dom.set_value("Input", "")
  dom.focus("Input")
  atlastk.broadcast_action("Refresh")

def ac_refresh(dom):
  dom.begin("Output", f"<div>Hello, {name}!</div>")
 
CALLBACKS = {
  "": ac_connect,
  "Submit": ac_submit,
  "Refresh": ac_refresh
}
 
atlastk.launch(CALLBACKS)
