curl -X GET localhost:8080/

echo "\n==============================================\n"

curl -X POST localhost:8080/opt/brain/listen \
    -d '{"body": "hello world", "namespace": "hqd"}' \
    -H 'Content-Type: application/json'

echo "\n==============================================\n"

curl -X POST localhost:8080/opt/brain/find \
    -d '{"body": "vlad", "namespace": "hqd"}' \
    -H 'Content-Type: application/json'

echo "\n==============================================\n"

curl -X POST localhost:8080/bin/text2_3d \
    -d '{"body": "How are you? I am fine. I am Vladislav and I am buy new car"}' \
    -H 'Content-Type: application/json'