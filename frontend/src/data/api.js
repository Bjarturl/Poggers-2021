import { API_URL } from "./constants";

const fetchUrl = async (url) => {
  return fetch(url)
    .then((response) => response.json())
    .then((data) => data);
};
const fetchAllEndpoints = async (endpoints, year) => {
  const data = [];
  for (const endpoint of endpoints) {
    data.push(await fetchUrl(`${API_URL}/data/${year}/${endpoint}`));
  }
  return data;
};

export const GET = {
  async dataByYear(year, name) {
    const url = `${API_URL}/data/${year}/${name}`;
    const data = await fetchUrl(url);
    return data;
  },

  async allData() {
    const url = `${API_URL}/data`;
    const data = await fetchUrl(url);
    return data;
  },

  async messagesByTimeData(year) {
    const endpoints = [
      "fjöldi_skilaboða_eftir_degi",
      "fjöldi_skilaboða_eftir_mánuðum",
      "fjöldi_skilaboða_eftir_tíma_dags",
    ];
    return await fetchAllEndpoints(endpoints, year);
  },

  async mostPopularData(year) {
    const endpoints = [
      "flest_skilaboð_send",
      "flestar_myndir_sendar",
      "meðallengd_skilaboða_í_orðum",
      "lengstu_skilaboðin_í_orðum",
    ];
    return await fetchAllEndpoints(endpoints, year);
  },

  async reactionData(year) {
    const endpoints = [
      "fékk_flest_reactions",
      "reactaði_oftast",
      "reactions_per_einstaklingur",
    ];
    return await fetchAllEndpoints(endpoints, year);
  },

  async nameData(year) {
    const endpoints = ["nafnið"];
    return await fetchAllEndpoints(endpoints, year);
  },

  //     async test() {
  //         "heildarfjöldi_mynda"
  // "heildarfjöldi_skilaboða"
  //         const url = `${API_URL}/data`
  //         const data = await fetchUrl(url)
  //         return data
  //     },
};
