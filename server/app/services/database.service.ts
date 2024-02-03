import { Db, MongoClient } from 'mongodb';
import 'reflect-metadata';
import { Service } from 'typedi';

export const DATABASE_URL =
    'mongodb+srv://JohnScrabble:8fNvAD6e7e0aN5g3@scrabblecluster.eqdnm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority';
export const DATABASE_NAME = 'scrabbleDB';


const STARTING_DATABASE: any[] = []

const DATABASE_COLLECTION_HIGH_SCORES = ''
@Service()
export class DatabaseService {
    private db: Db;
    private client: MongoClient;

    async start(url: string = DATABASE_URL): Promise<MongoClient | null> {
        try {
            const client = await MongoClient.connect(url);
            this.client = client;
            this.db = client.db(DATABASE_NAME);
        } catch {
            throw new Error('Database connection error');
        }

        if ((await this.db.collection(DATABASE_COLLECTION_HIGH_SCORES).countDocuments()) === 0) {
            await this.populateHighScores();
        }

        return this.client;
    }

    async closeConnection(): Promise<void> {
        return this.client.close();
    }

    async populateHighScores(): Promise<void> {
        for (const highScore of STARTING_DATABASE) {
            await this.db.collection(DATABASE_COLLECTION_HIGH_SCORES).insertOne(highScore);
        }
    }
    get database(): Db {
        return this.db;
    }
}