# CyberStreak v2.0

> Thank you for your report !
>
> You can now create your own challenges, delete them, deactivate / activate them.
>
> xXx-michel-xXx
>
> http://challs.dvc.tf:5002
>
> *Brute force is strictly forbidden and useless.*
>

- Create a account with a simple username like `aa`
- Create a new challenge with a simple image filename like `a`
- Check the path of the image : `961b6dd3ede3cb8ecbaacbd68de040cd78eb2ed5889130cceb4c49268ea4d506/9d607a663f3e9b0a90c3c8d4426640dc`
- Crack the first hash (with https://crackstation.net/ for example) : `SHA256(aa) == 961b6dd3ede3cb8ecbaacbd68de040cd78eb2ed5889130cceb4c49268ea4d506`
- Crack the second hash : `MD5(a3) == 9d607a663f3e9b0a90c3c8d4426640dc`
- The first challenge give us the name of the image with the flag : `flaggggggggggggggggggggggg.png` and the ID of the challenge : `2`
- Infer that the path of the flag is : `SHA256(xXx-michel-xXx)/MD5(flaggggggggggggggggggggggg.png2)`
- Path : `ffc2e03c7152165f02a4cca8fe426f9f0f8c9ea4a02a2077ecaeb4fdfeeed92e/7e0c7ec9c02bffca0ff9a9dc26f02f5b`
