import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sol", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255))
cv2.putText(img, "Mercurio", (110, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (190, 175), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Tierra", (280, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Marte", (370, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (480, 70), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturno", (700, 110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Urano", (950, 130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptuno", (1100, 140), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.imshow("Output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_system_with_name.jpg", img)

cv2.destroyAllWindows()
