#!/bin/bash

# Set the time threshold for pod deletion (4 hours)
THRESHOLD=$(date -d '-4 hours' --utc +%s)

# Get the list of pods older than the threshold and store their names in an array
PODS=$(kubectl get pods --all-namespaces --field-selector=status.startTime<=$(date -d '-4 hours' -Ins --utc | sed 's/+0000/Z/') --output=jsonpath='{range .items[*]}{.metadata.namespace}/{.metadata.name}{"\n"}{end}')

# Loop through the pods and delete them
for POD in ${PODS}; do
    NAMESPACE=$(echo ${POD} | cut -d'/' -f1)
    NAME=$(echo ${POD} | cut -d'/' -f2)
    START_TIME=$(kubectl get pod ${NAME} -n ${NAMESPACE} -o jsonpath='{.status.startTime}')
    START_TIME_SEC=$(date -d ${START_TIME} --utc +%s)

    if [ ${START_TIME_SEC} -le ${THRESHOLD} ]; then
        echo "Deleting pod ${POD}..."
        kubectl delete pod ${NAME} -n ${NAMESPACE}
    fi
done
