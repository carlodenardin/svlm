import gradio as gr

def _update_test_output(input_val, tests):
    """
    Callback to update the output of a test based on selected input.
    """
    if input_val == "Select Input":
        return gr.update(value=""), gr.update(choices=["Select Input"] + [str(test['input']) for test in tests])

    for test_case in tests:
        if str(test_case['input']) == input_val:
            output = str(test_case['output'])
            new_choices = [str(test['input']) for test in tests]
            return gr.update(value=output), gr.update(choices=new_choices)
    
    return gr.update(value="Output non trovato."), gr.update()

def create_interactive_test_block(tests, label):
    """
    Create a Gradio block for interactive test inputs and outputs.
    """
    test_inputs = [str(test['input']) for test in tests]
    dropdown_choices = ["Select Input"] + test_inputs

    with gr.Row():
        test_input_dropdown = gr.Dropdown(
            choices=dropdown_choices,
            label=label,
            value="Select Input",
            interactive=True
        )
        test_output_box = gr.Textbox(label="Output")
    
    tests_state = gr.State(value=tests)
    
    test_input_dropdown.change(
        fn=_update_test_output,
        inputs=[test_input_dropdown, tests_state],
        outputs=[test_output_box, test_input_dropdown]
    )