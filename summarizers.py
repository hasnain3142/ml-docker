import os
from abc import ABCMeta, abstractmethod
from typing import Tuple, Union
from loguru import logger
from transformers import pipeline

class BaseSummarizer(metaclass=ABCMeta):
    """
    Abstract class for Summarizer
    """
    @abstractmethod
    def predict(
        self,
        text: Union[list, str],
        **kwargs,
    ):
        """To Be overwritten"""
        pass

class TransformersSummarizer(BaseSummarizer):
    """
    Transformer based model to summarize the documents using the HuggingFace's transformers framework
    You can use these models for summarization
    """
    register_models: Tuple[str, ...] = (
        "facebook/bart-large-cnn",
        "google/pegasus-cnn_dailymail",
        "sshleifer/distilbart-cnn-12-6",
    )
    def __init__(
        self,
        model_name: str,
        summary_min_length: int = 50,
        summary_max_length: int = 1000,
    ) -> None:
        """
        Initializes a summarization models if not initialized already.
        Args:
            model_name:
            summary_min_length:
            summary_max_length:
        """
        self.__model_name: str = model_name
        self.max_length: int = summary_max_length
        self.min_length: int = summary_min_length
        logger.info(f"Loading summarization model={self.__model_name}")
        assert self.__model_name in self.register_models, f"{self.__model_name} is not a supported model"
        model_path = "models/" + self.__model_name.replace("/", "-")
        if not os.path.exists(model_path):
            # Create the directory
            os.makedirs(model_path)
            download_model(model_path, self.__model_name)
            logger.info(f"model downloaded={model_path}")
        self.__loaded_model = pipeline("summarization", model=model_path)
        logger.info(f"model loaded={model_path}")


    def predict(
        self,
        text: Union[list, str],
        batch_size=1,
        **kwargs,
    ):
        """
        Generates a summary for the provided text
        Args:
            text (list or str): Text to make summary of
            summary_max_length (int): Maximum length of summary. If not given,
                                    will be calculated as 0.7 times word length of text. Defaults to None.
            summary_min_length (int): Minimum length of summary. If not given,
                                    will be calculated as 0.5 times word length of text. Defaults to None.
            generate_single_summary (bool): If True, will generate a single summary for the whole text.
        Returns:
            str or list: summary of provided text
        """
        single_summary = isinstance(text, str)
        if single_summary:
            text = [text]
        summaries = self.__loaded_model(
            text,
            min_length=self.min_length,
            max_length=self.max_length,
            do_sample=False,
            truncation=False,
            batch_size=batch_size,
        )
        summaries = [summary["summary_text"] for summary in summaries]
        if single_summary:
            summaries = summaries[0]
        return summaries
    
    def __call__(self, text: Union[list, str]):
        """
        Call function
        Args:
            text:
            summary_max_length:
            summary_min_length:
        Returns:
        """
        return self.predict(text)
    
def download_model(model_path, model_name):
    """Download a Hugging Face model to the specified directory"""
    model = pipeline("summarization", model=model_name)
    # Save the model to the specified directory
    model.save_pretrained(model_path)