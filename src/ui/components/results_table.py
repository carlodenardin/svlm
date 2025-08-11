import gradio as gr
import pandas as pd

def create_results_table_block(results, label):
    """
    Create a block with a table of test results.
    """
    if not results:
        gr.Markdown(f"Nessun risultato disponibile per i test **{label}**.")
        return

    df = pd.DataFrame(results)
    
    num_tests = len(df)
    num_passed = df['success'].sum()
    num_failed = num_tests - num_passed
    success_rate = f"{(num_passed / num_tests) * 100:.0f}%" if num_tests > 0 else "0%"

    summary_text = f"{label} Test ({num_passed}/{num_tests} -> {success_rate})"
    
    def style_row_by_success(row):
        color = 'green' if row['success'] else 'red'
        return [f'color: {color};'] * len(row)

    styled_df = df.style.apply(style_row_by_success, axis=1)

    gr.Markdown(f"### {summary_text}")
    gr.Dataframe(
        value=styled_df,
        interactive=False,
    )