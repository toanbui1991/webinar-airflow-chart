from kubernetes import client, config, utils


config.load_kube_config()

k8s_client = client.ApiClient()
yaml_file = './kubernetes_selenium/selenium-node-chrome-deployment.yaml'
deployment = utils.create_from_yaml(k8s_client, yaml_file)

deployment.spec.replicas = 3

# patch the deployment
DEPLOYMENT_NAME = "selenium-node-chrome-deployment"
resp = k8s_client.patch_namespaced_deployment(
    name=DEPLOYMENT_NAME, namespace="default", body=deployment
)

print("\n[INFO] increase deployment's pod to 3.\n")
print("%s\t%s\t\t\t%s\t%s" % ("NAMESPACE", "NAME", "REVISION", "IMAGE"))
print(
    "%s\t\t%s\t%s\t\t%s\n"
    % (
        resp.metadata.namespace,
        resp.metadata.name,
        resp.metadata.generation,
        resp.spec.replicas,
    )
)