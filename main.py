from src.ui.interface import create_gradio_interface

if __name__ == "__main__":
    demo = create_gradio_interface()
    demo.launch(share = False)