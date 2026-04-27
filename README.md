# deploy kind
kind delete cluster --name <your-cluster-name>
kind create cluster --name <your-cluster-name> --config kind-config.yaml

# install nginx controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

# install argocd with helm
helm upgrade --install argocd  argo/argo-cd -n argocd --create-namespace -f values-argo.yaml