# Liste de tâches

Il s'agit d'une application simple qui permet de créer une liste de tâches que l'utilisateur peut consulter, marquer comme réalisées ou supprimer si elles ne sont plus nécessaires.

## Implémentation de l'application

En premier lieu, nous clonons le répertoire sur notre machine.

```         
git clone https://github.com/carlosconde775/Liste-de-taches.git
```

Après on va au repertoire du projet.

```         
cd Liste-de-taches
```

## Implémentation de l'application dans Docker

On construit l'image docker:

```         
docker build -t taches .
```

On vérifie si cela a été fait.

```         
docker images
```

On lance le container.

```         
docker run -p 5000:5000 -t taches 
```

C'est possible de tester le service à l'aide d'un navigateur web : [http://localhost:5000](#0)

## Implémentation de l'application dans Minikube

### Création d'une deployment et un service en utilisant une yaml file

On applique le deployment:

```         
kubectl apply -f taches-deployment.yml
```

On applique le service node port:

```         
kubectl apply -f taches-service.yml
```

ou

On applique le service de type loadbalancer:

```         
kubectl apply -f loadbalancing-service.yml
```

Puis on teste si cela fonctionne correctement.

Il faut, d'abord, lancer le tunnel minikube pour pouvoir acceder localement à kubernetes

```         
minikube tunnel
```

Puis on teste le service web à l'aide d'un navigateur web : [http://localhost:8080](http://localhost:5000/)

### Utilisation d'Ingress

Il faut autoriser le NGINX Ingress controller:

```         
minikube addons enable ingress
```

On vérifie que le NGINX Ingress controller a été lancé.

```         
kubectl get pods -n kube-system
```

Il faur préalablement créer un Deployment et l'exposer via NodePort (et pas loadbalancer).

Pour tester si cela marche bien:

```         
kubectl apply -f taches-ingress.yml
```

Retrouver l'adresse IP d'Ingress:

```         
kubectl get ingress
```

```         
NAME                 CLASS    HOSTS                  ADDRESS        PORTS   AGE

taches-ingress      nginx   taches.info         192.168.49.2   80      18m
```

Sur Linux: éditer le fichier `/etc/hosts`et ajouter:

`ADDRESS     HOSTS`

Pour tester sur le navigateur:

[http://taches.info/](http://myservice.info/){.uri}

Sur Windows : éditer le fichier `c:\windows\system32\drivers\etc\hosts`, ajouter

`127.0.0.1 taches.info`

Autoriser le tunnel minikube :

```         
minikube addons enable ingress-dns
```

```         
minikube tunnel
```

Puis tester sur le navigateur:

[http://taches.info/](http://myservice.info/){.uri}
