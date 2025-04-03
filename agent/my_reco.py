from maa.agent.agent_server import AgentServer
from maa.custom_recognition import CustomRecognition
from maa.context import Context
import math

@AgentServer.custom_recognition("IsSimilar")
class IsSimilar(CustomRecognition):
    def analyze(
        self,
        context: Context,
        argv: CustomRecognition.AnalyzeArg,
    ) -> CustomRecognition.AnalyzeResult:

        reco_detail = context.run_recognition(
            "识别票",
            argv.image,
            )
                        # reco_detail = context.run_recognition(
        #     "",
        #     argv.image,
        #     pipeline_override={"MyCustomOCR": {"recognition": "OCR","expected": "投1次",
        #                         "index": 1,
        #                         }},
        #     )
        # context is a reference, will override the pipeline for whole task
        # context.override_pipeline({"MyCustomOCR": {"roi": [1, 1, 114, 514]}})
        # context.run_recognition ...
        # print(steps_manhattan)
        # # make a new context to override the pipeline, only for itself
        # new_context = context.clone()
        # new_context.override_pipeline({"MyCustomOCR": {"roi": [100, 200, 300, 400]}})
        # reco_detail = new_context.run_recognition("MyCustomOCR", argv.image)

        click_job = context.tasker.controller.post_click(10, 20)
        click_job.wait()

        # context.override_next(argv.node_name, ["TaskA", "TaskB"])
        
        return CustomRecognition.AnalyzeResult(
            reco_detail.box, detail="Hello World!"
        )
