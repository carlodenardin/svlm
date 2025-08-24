from src.ui.interface import create_gradio_interface
from src.utils.utils import creare_report_excel

if __name__ == "__main__":

    creare_report_excel("results/human_eval")

    demo = create_gradio_interface()
    demo.launch()