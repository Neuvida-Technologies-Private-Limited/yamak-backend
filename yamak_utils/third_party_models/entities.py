from abc import ABC
from abc import abstractmethod
from enum import Enum


class ModelNameEnum(Enum):
    TIIUAE_FALCON_7B_INSTRUCT = "tiiuae/falcon-7b-instruct"
    # CARPERAI_STABLE_VICUNA_13B_DELTA  = "CarperAI/stable-vicuna-13b-delta"
    # OPENASSISTANT_FALCON_40B_SFT_TOP1_560 = "OpenAssistant/falcon-40b-sft-top1-560"
    # OPENASSISTANT__FALCON_7B_SFT_TOP1_696 = "OpenAssistant/falcon-7b-sft-top1-696"
    # OPENASSISTANT_OASST_SFT_7_LLAMA_30B_XOR = "OpenAssistant/oasst-sft-7-llama-30b-xor"
    # AMAZON_LIGHTGPT = "amazon/LightGPT"
    # DATABRICKS_DOLLY_V2_12B = "databricks/dolly-v2-12b"
    # H2OAI_H2OGPT_OASST1_512_12B = "h2oai/h2ogpt-oasst1-512-12b"
    # LMSYS_VICUNA_13B_DELTA_v1_1 = "lmsys/vicuna-13b-delta-v1_1"
    # MOSAICML_MPT_30B_CHAT = "mosaicml/mpt-30b-chat"
    # MOSAICML_MPT_7B_CHAT = "mosaicml/mpt-7b-chat"
    # MOSAICML_MPT_7B_INSTRUCT = "mosaicml/mpt-7b-instruct"
    # MOSIACML_MPT_7B_STORYWRITER = "mosaicml/mpt-7b-storywriter"
    # STABILITYai_STABLELM_TUNED_ALPHA_7B = "stabilityai/stablelm-tuned-alpha-7b"


class ModelClient(ABC):

    @abstractmethod
    def get_inference(self, model_input: str, model_name: ModelNameEnum) -> str:
        pass
