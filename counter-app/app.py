import requests

url = "https://camo.githubusercontent.com/795c825925f5daf56c6680f8004ad1a2c145a8196d12f50bbc1f4bfe771ac0c9/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d616264756c6c616879616c63696e266c6162656c3d56697369746f727326636f6c6f723d376630306666267374796c653d666c6174"

for _ in range(1000):
    response = requests.get(url)
    print(response.text)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
