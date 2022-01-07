from ezkubernetes import DeploymentWriter

class OriginDeploymentWriter(DeploymentWriter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _replace_placeholders(self, config, name, text):
        text = text.replace("NAME_PLACEHOLDER", name)
        text = text.replace("REDI_NODE_PLACEHOLDER", config["redi_node"])
        text = text.replace("REDI_PORT_PLACEHOLDER", config["redi_port"])
        text = text.replace("NODE_PLACEHOLDER", config["node"])
        text = text.replace("PORT_PLACEHOLDER", config["port"])
        text = text.replace("PVC_PLACEHOLDER", config["pvc"])
        return text

    def _get_deployment_name(self, config):
        N = config["node"].split(".")[0].split("-")[-1]
        return f"{self.app_name}-{N}-{config['port']}"

if __name__ == "__main__":
    origin_configs = [
        {
            "node": "k8s1-pb10.ultralight.org", 
            "port": "2811",
            "pvc": "pvc-xrootd-data-lake-origin-caltech-k8s1-pb10-ultralight-org-persistent-7",
            "redi_node": "k8s1-pb10.ultralight.org",
            "redi_port": "9001"
        }, 
        # {
        #     "node": "k8s1-pb10.ultralight.org", 
        #     "port": "2812",
        #     "pvc": "pvc-xrootd-data-lake-origin-caltech-k8s1-pb10-ultralight-org-persistent-8",
        #     "redi_node": "k8s1-pb10.ultralight.org",
        #     "redi_port": "9001"
        # }, 
    ]
    deployment_writer = OriginDeploymentWriter(
        base_dir="./", 
        template_dir="templates", 
        app_name="us-cms-datalake-origin", 
        namespace="cms-admin",
        configs=origin_configs
    )
    deployment_writer.write()
