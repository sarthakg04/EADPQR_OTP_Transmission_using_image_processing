# EADPQR_OTP_Transmission_using_image_processing
EADPQR(Enhanced Authentication for Dynamic Password generation using QRCode)
EADPQR is an Enhanced method for generation and transmission of OTP(One Time Password) over any protocol.
EADPQR Working:-
1) EADPQR generates a "N" Digit OTP (Input from Client).
2) This generated OTP is generated by a Randomized matrix method.
3) The Generated OTP is converted to a QR Code.
4) Another SKIN_OTP ie. a temporary OTP is generated by the same method.
5) This OTP is Superimposed over the Primary QR to Distort the QR.
6) The Distorted QR is Transmitted over the Connection which surpasses all the Decryption patterns using OpenCV libraries.
7) The Transmitted OTP can be Retrived by end user with Decryption Algorithm.
