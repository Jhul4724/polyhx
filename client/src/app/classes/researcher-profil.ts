export class Item {
    lastName: string;
    firstName: string;
    itemName: string;
    itemDescription: string;
    itemImage: string;
    itemPrice: string;
    itemNumber: number;
    itemType: string;
    username: string;
    quantity: number;
  }

export function FillItems(): Item[] {
    const exampleList: Item[] = [
        {
          lastName: "Uh",
          firstName: "Julian",
          itemName: "Exotic Fruit Sampler",
          itemDescription: "Sampler pack of rare and exotic fruits for a unique garden.",
          itemImage: "https://media.istockphoto.com/id/185262648/fr/photo/pomme-rouge-avec-feuilles-isol%C3%A9-sur-fond-blanc.jpg?s=1024x1024&w=is&k=20&c=Xo5ONBi4HjBOCI4UfelgVSLA6RaDqJM689Re9CeOh5w=",
          itemPrice: "$45.00",
          itemNumber: 126,
          itemType: "mixed",
          username: "julian_uh",
          quantity: 4
        },
        {
          lastName: "Uh",
          firstName: "Julian",
          itemName: "Heirloom Tomato Trio",
          itemDescription: "Set of heirloom tomato plants with distinct flavors and colors.",
          itemImage: "https://media.istockphoto.com/id/1157946861/fr/photo/fraise-de-baie-rouge-disolement.jpg?s=1024x1024&w=is&k=20&c=kodA2AQGJd7a4mRCqqYWRlFCf01R_DZfAKHlwWR-VYk=",
          itemPrice: "$35.00",
          itemNumber: 127,
          itemType: "vegetable",
          username: "julian_uh",
          quantity: 10
        },
        {
          lastName: "Uh",
          firstName: "Julian",
          itemName: "Tropical Paradise Bundle",
          itemDescription: "Bundle of tropical fruit trees, including mango, banana, and pineapple.",
          itemImage: "https://media.istockphoto.com/id/185262648/fr/photo/pomme-rouge-avec-feuilles-isol%C3%A9-sur-fond-blanc.jpg?s=1024x1024&w=is&k=20&c=Xo5ONBi4HjBOCI4UfelgVSLA6RaDqJM689Re9CeOh5w=",
          itemPrice: "$55.00",
          itemNumber: 128,
          itemType: "mixed",
          username: "julian_uh",
          quantity: 1
        },
        {
          lastName: "Uh",
          firstName: "Julian",
          itemName: "Colorful Pepper Pack",
          itemDescription: "Pack of colorful bell peppers for a vibrant garden display.",
          itemImage: "https://media.istockphoto.com/id/1157946861/fr/photo/fraise-de-baie-rouge-disolement.jpg?s=1024x1024&w=is&k=20&c=kodA2AQGJd7a4mRCqqYWRlFCf01R_DZfAKHlwWR-VYk=",
          itemPrice: "$30.00",
          itemNumber: 129,
          itemType: "vegetable",
          username: "julian_uh",
          quantity: 8
        },
        {
          lastName: "Uh",
          firstName: "Julian",
          itemName: "Aromatic Herb Collection",
          itemDescription: "Collection of aromatic herbs for culinary and medicinal use.",
          itemImage: "https://media.istockphoto.com/id/1157946861/fr/photo/fraise-de-baie-rouge-disolement.jpg?s=1024x1024&w=is&k=20&c=kodA2AQGJd7a4mRCqqYWRlFCf01R_DZfAKHlwWR-VYk=",
          itemPrice: "$40.00",
          itemNumber: 130,
          itemType: "mixed",
          username: "julian_uh",
          quantity: 3
        }
      ];

    return exampleList;
}
