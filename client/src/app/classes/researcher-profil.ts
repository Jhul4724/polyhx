import { Expertise } from './expertise';

export class ResearcherProfil {
    name: string;
    phoneNumber: number;
    email: string;
    university: string;
    departement: string;
    city: string;
    province: string;
    expertises: Expertise[];
}

export function FillProfiles(): ResearcherProfil[] {
    const profiles: ResearcherProfil[] = [];
    for (let i = 0; i < 10; i++) {
        const profile = new ResearcherProfil();
        profile.name = 'Abderrahmane Grou';
        profile.phoneNumber = 5145378110;
        profile.email = 'abdougr@polymtl.ca';
        profile.university = 'Polytechnique Montreal';
        profile.departement = 'Genie informatique & genie logiciel';
        profile.city = 'Montreal';
        profile.province = 'Quebec';
        profile.expertises = [new Expertise('Machine Learning'), new Expertise('NLP'), new Expertise('Visualisation de donnees')];
        profiles.push(profile);
    }

    return profiles;
}
