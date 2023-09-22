// Récupération des pièces depuis notre fichier JSON
const reponse = await fetch("pieces-autos.json");
const pieces = await reponse.json();

for (let i = 0; i<pieces.length; i++) {



    const article = pieces[i];
    // Récupération de l'élément du DOM qui accueillera les fiches
    const sectionFiches = document.querySelector(".fiches");
    // Création d’une balise dédiée à une pièce automobile
    const pieceElement = document.createElement("article");
    // Création des balises 
    const imageElement = document.createElement("img");
    imageElement.src = article.image;
    const nomElement = document.createElement("h2");
    nomElement.innerText = article.nom;
    const prixElement = document.createElement("p");
    prixElement.innerText = `Prix: ${article.prix} € (${article.prix < 35 ? "€" : "€€€"})`;
    const categorieElement = document.createElement("p");
    categorieElement.innerText = article.categorie ?? "(aucune catégorie)";
    const descriptionElement = document.createElement("p");
    descriptionElement.innerText = article.description ?? "Pas de description pour le moment.";
    const stockElement = document.createElement("p");
    stockElement.innerText = article.disponibilite ? "En stock" : "Rupture de stock";

    // Notre page web contient une balise section avec la classe “fiches” 
    // que nous utiliserons comme parent. 
    // Nous la récupérons grâce à querySelector
    sectionFiches.appendChild(pieceElement);
    // appendChild ajout à la section selectionné les const où l'on a stocké les infos du Json
    pieceElement.appendChild(imageElement);
    pieceElement.appendChild(nomElement);
    pieceElement.appendChild(prixElement);
    pieceElement.appendChild(categorieElement);
    pieceElement.appendChild(descriptionElement);
    pieceElement.appendChild(stockElement)

}

// Sélectionnez l'élément du DOM qui a la classe CSS "btn-trier" et stockez-le dans la variable boutonTrier.
const boutonTrier = document.querySelector(".btn-trier");

// Ajoutez un écouteur d'événements qui réagit lorsque l'utilisateur clique sur le bouton "Trier".
boutonTrier.addEventListener("click", function() {
    // Créez une copie du tableau "pieces" en utilisant Array.from().
    const piecesOrdonnees = Array.from(pieces);

    // Triez le tableau "piecesOrdonnees" par ordre croissant de prix.
    piecesOrdonnees.sort(function(a, b) {
        // La fonction de comparaison compare les prix de deux articles a et b.
        // Si a.prix est inférieur à b.prix, la fonction renvoie un nombre négatif,
        // si a.prix est supérieur à b.prix, elle renvoie un nombre positif,
        // et si les prix sont égaux, elle renvoie 0.
        return a.prix - b.prix;
    });

    // Affichez le tableau trié dans la console du navigateur.
    console.log(piecesOrdonnees);
});


const boutonFiltrer = document.querySelector(".btn-filtrer");
boutonFiltrer.addEventListener("click", function(){

    const piecesFiltrees = pieces.filter(function (pieces){
        return pieces.prix <= 35;
    });
    console.log(piecesFiltrees)
});

const boutonFiltrerDescription = document.querySelector(".btn-filter-description");
boutonFiltrerDescription.addEventListener("click", function(){

    const piecesFiltreesDescription= pieces.filter(function (pieces){
        return pieces.description;
    });
    console.log(piecesFiltreesDescription)
});

const boutonTrierDesc = document.querySelector(".btn-trier-desc");
boutonTrierDesc.addEventListener("click", function(){

    const piecesOrdonnéesDesc = Array.from(pieces);
    piecesOrdonnéesDesc.sort(function(a,b){
        return b.prix-a.prix;
    });
    console.log(piecesOrdonnéesDesc)
});