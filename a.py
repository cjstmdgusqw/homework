import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img = cv2.imread('Untitled.jpeg')
results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='person']

tmp_img = cv2.imread('Untitled.jpeg')
print(tmp_img.shape)
cropped = tmp_img[int(result[0][1]):int(result[0][3]), int(result[0][0]):int(result[0][2])]

cv2.imwrite('people.png', cropped)
cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (255,255,255))
cv2.imwrite('result.png', tmp_img)

cropped2 = tmp_img[int(result[1][1]):int(result[1][3]), int(result[1][0]):int(result[1][2])]

cv2.imwrite('people2.png', cropped2)
cv2.rectangle(tmp_img, (int(results.xyxy[0][1][0].item()), int(results.xyxy[0][1][1].item())), (int(results.xyxy[0][1][2].item()), int(results.xyxy[0][1][3].item())), (255,255,255))
cv2.imwrite('result2.png', tmp_img)

cropped3 = tmp_img[int(result[2][1]):int(result[2][3]), int(result[2][0]):int(result[2][2])]

cv2.imwrite('people3.png', cropped3)
cv2.rectangle(tmp_img, (int(results.xyxy[0][2][0].item()), int(results.xyxy[0][2][1].item())), (int(results.xyxy[0][2][2].item()), int(results.xyxy[0][2][3].item())), (255,255,255))
cv2.imwrite('result3.png', tmp_img)

cropped4 = tmp_img[int(result[3][1]):int(result[3][3]), int(result[3][0]):int(result[3][2])]

cv2.imwrite('people4.png', cropped4)
cv2.rectangle(tmp_img, (int(results.xyxy[0][3][0].item()), int(results.xyxy[0][3][1].item())), (int(results.xyxy[0][3][2].item()), int(results.xyxy[0][3][3].item())), (255,255,255))
cv2.imwrite('result4.png', tmp_img)

cropped5 = tmp_img[int(result[4][1]):int(result[4][3]), int(result[4][0]):int(result[4][2])]

cv2.imwrite('people5.png', cropped5)
cv2.rectangle(tmp_img, (int(results.xyxy[0][4][0].item()), int(results.xyxy[0][4][1].item())), (int(results.xyxy[0][4][2].item()), int(results.xyxy[0][4][3].item())), (255,255,255))
cv2.imwrite('result5.png', tmp_img)




