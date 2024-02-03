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
          itemImage: "exotic_fruit_sampler_image.jpg",
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
          itemImage: "heirloom_tomato_trio_image.jpg",
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
          itemImage: "tropical_paradise_bundle_image.jpg",
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
          itemImage: "colorful_pepper_pack_image.jpg",
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
          itemImage: "aromatic_herb_collection_image.jpg",
          itemPrice: "$40.00",
          itemNumber: 130,
          itemType: "mixed",
          username: "julian_uh",
          quantity: 3
        }
      ];

    return exampleList;
}
