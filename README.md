<h1>Presenter-Centric Image Collection and Annotation: Enhancing Accessibility for the Visually Impaired</h1>

<img src="resources/dataset_samples.jpg" align="center" />


This repository contains the proposed dataset of the paper **[Presenter-Centric Image Collection and Annotation: Enhancing Accessibility for the Visually Impaired]()**.

We propose an approach to collect data automatically and a protocol to annotate this data specifically for this audience, aiming to support the development of Assistive Technology systems. We provide access to our three datasets: complete dataset, single person dataset, and annotated single person dataset.The complete dataset contains 10.939 images, the single person dataset contains 5689 images and the annotated single person dataset contains 570 images, each accompanied by three descriptive annotations. The images were collected from [youtube.com](https://www.youtube.com/). 

If you find this code useful for your research, please cite the paper:

```
adicionar depois
```

---

Access Datasets:
===
We're giving you a script along with text files that list the filenames for each image in the dataset. These filenames include important info like YouTube ID and frame ID, which the script uses to fetch the images.

- ### 1 . Install requirements
    You can find the necessary libraries to run the Python script in the `dataset/requirements.txt` file.


    ```bash
    pip install -r requirements.txt
    ```

- ### 2 . Running the script
    To obtain the images from the dataset, run the `dataset/collect_images.py` file. For the Complete Dataset, use '1' as the argument, '2' for the single person dataset, and '3' for the annotated single person dataset. You can find the annotations for the annotated single person dataset in the `dataset/annotations.json` file.
    ```bash
    python collect_images.py 1
    python collect_images.py 2
    python collect_images.py 3
    ```

---

Following the steps provided, you'll acquire the images from the datasets.



Contact
===

Authors
---

* Luísa Ferreira - BsC student - UFV - luisa.ferreira@ufv.br.br
* Daniel Fernandes - PhD student - UFV - daniel.louzada@ufv.br
* Michel Silva - Assistant Professor at Universidade Federal de Viçosa (UFV) - michel.m.melo@ufv.br

Institution
---

Universidade Federal de Viçosa (UFV)  
Departamento de Ciência da Computação  
Viçosa- Minas Gerais -Brazil 

Laboratory
---
![MaVILab](https://mavilab-ufv.github.io/images/mavilab-logo.png) | ![UFV](https://cdn.discordapp.com/attachments/729689711416967239/844210892916523018/Ygemzly2XsP3gzFbXjFyExvD00B3rBvPbDEOoNOB-4uL4NLF1YKM6kiypik1H4koNc5_sNVAAAy_PDq_kmh_CRmn1dvC1uyeckCs.png)
--- | ---


**MaVILab:** Machine Vision and Intelligence Laboratory
https://mavilab-ufv.github.io/

---

Acknowledgements
===

We would like to thanks CAPES, FAPEMIG and CNPq for funding this work; Ricson Luiz Oliveira Vilaça for fine-tunning the scene classification CNN; and our tireless annotators Allan Lopes, Júlia Vieira, Júlia Lopes, and Sophia Jorge.

### Enjoy it! :smiley:
