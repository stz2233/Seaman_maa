from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context
num=66
biao=[15,28,30,37,53,65]
int_1=65
dd=0
deshu=False
@AgentServer.custom_action("my_action_111")
class MyCustomAction(CustomAction):

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:
        if(int_1 > num):
            int_1=int_1-num
        for cell in biao:
            if cell -  int_1 > 0:
                if cell -  int_1 < 6:
                    dd=cell-int_1
                    deshu=True
        img = context.tasker.controller.post_screencap().wait().get()
        if(deshu):
            reco_detail = context.run_recognition(
                "特殊投一次",
                img,
                )
            
            context.run_action( )
        


        return True
