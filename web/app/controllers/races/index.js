import Ember from 'ember';
import _ from 'lodash/lodash';

export default Ember.Controller.extend({
  splitByClan: false,
  splitByGender: false,

  tableData: Ember.computed('model.races', 'model.stats', 'splitByClan', 'splitByGender', function() {
    // Reduce races into a plain object for quick id lookups
    let races = this.get('model.races').reduce((val, race) => {
      val[race.get('id')] = {
        id: race.get('id'),
        name: race.get('name'),
        slug: race.get('slug'),
        clans: [
          { name: race.get('clan_1'), num_characters: [0, 0] },
          { name: race.get('clan_2'), num_characters: [0, 0] },
        ],
        num_characters: race.get('num_characters'),
      };
      return val;
    }, {});

    // Fill in statistics information
    this.get('model.stats').forEach((stat) => {
      let race = races[stat.race];
      let clan = race.clans[stat.clan - 1];
      clan.num_characters[stat.gender - 1] += stat.num_characters;
    });

    // Make it into an array of values
    let data = _.values(races);

    // If requested, split the data by clans
    if (this.get('splitByClan')) {
      let newData = [];
      data.forEach((race) => {
        race.clans.forEach((clan) => {
          let d = _.clone(race);
          d.name += ' - ' + clan.name;
          d.num_characters = clan.num_characters.reduce((cur, val) => { return cur + val; });
          d._clan = clan;
          newData.push(d);
        });
      });
      data = newData;
    }

    // If requested, split the data by genders
    if (this.get('splitByGender')) {
      let newData = [];
      data.forEach((race) => {
        ['\u2642', '\u2640'].forEach((symbol, gender) => {
          let d = _.clone(race);
          d.name += ' ' + symbol;
          if (d._clan) {
            d.num_characters = d._clan.num_characters[gender];
          } else {
            d.num_characters = d.clans.reduce((cur, clan) => { return cur + clan.num_characters[gender]; }, 0);
          }
          newData.push(d);
        });
      });
      data = newData;
    }

    return data;
  }),
  chartData: Ember.computed('tableData', function() {
    return this.get('tableData').map((race) => {
      return { label: race.name, value: race.num_characters };
    });
  }),
});
