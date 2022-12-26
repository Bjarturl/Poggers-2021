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
      "fjoldi_skilaboda_eftir_degi",
      "fjoldi_skilaboda_eftir_manudum",
      "fjoldi_skilaboda_eftir_tima_dags",
    ];
    return await fetchAllEndpoints(endpoints, year);
  },

  async mostPopularData(year) {
    const endpoints = [
      "flest_skilabod_send",
      "flestar_myndir_sendar",
      "medallengd_skilaboda_i_ordum",
      "lengstu_skilabodin_i_ordum",
    ];
    return await fetchAllEndpoints(endpoints, year);
  },

  async reactionData(year) {
    const endpoints = [
      "fekk_flest_reactions",
      "reactadi_oftast",
      "reactions_per_einstaklingur",
    ];
    return await fetchAllEndpoints(endpoints, year);
  },

  async nameData(year) {
    const endpoints = ["nafnid"];
    return await fetchAllEndpoints(endpoints, year);
  },

  async allTimeData(year) {
    const endpoints = ["heildarfjoldi_mynda", "heildarfjoldi_skilaboda"];
    return await fetchAllEndpoints(endpoints, year);
  },

  async battleStats(year) {
    const endpoints = ["battle_stats"];
    return await fetchAllEndpoints(endpoints, year);
  },

  //     async test() {
  //         "heildarfjoldi_mynda"
  // "heildarfjoldi_skilaboða"
  //         const url = `${API_URL}/data`
  //         const data = await fetchUrl(url)
  //         return data
  //     },
};
