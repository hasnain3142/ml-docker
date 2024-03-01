from summarizers import TransformersSummarizer

model = TransformersSummarizer("sshleifer/distilbart-cnn-12-6")

def model_inference(text: str):
    #--
    #any preprocessing stuff before invoking the model
    summary = model(text)
    return summary