import Ember from 'ember';
import _ from 'lodash/lodash';

export default Ember.Controller.extend({
  splitByClan: false,
  splitByGender: false,
  filterByRace: null,

  data: Ember.computed('model.races', 'model.stats', 'splitByClan', 'splitByGender', 'filterByRace', function() {
    let data = this.get('model.races').map((race) => {
      return {
        race: race,
        stats: this.get('model.stats').filterBy('race', parseInt(race.get('id'))),
      };
    });

    if (this.get('filterByRace')) {
      data = data.filterBy('race.id', this.get('filterByRace.id'));
    }

    if (this.get('splitByClan')) {
      data = data.reduce((cur, val) => {
        [1, 2].forEach((clan_id) => {
          let d = _.clone(val);
          d.clan = { id: clan_id, name: d.race.get('clan_' + clan_id) };
          d.stats = d.stats.filterBy('clan', clan_id);
          cur.push(d);
        });
        return cur;
      }, []);
    }

    if (this.get('splitByGender')) {
      let genders = [
        { id: 1, name: "Male", symbol: '\u2642' },
        { id: 2, name: "Female", symbol: '\u2640' },
      ];
      data = data.reduce((cur, val) => {
        genders.forEach((gender) => {
          let d = _.clone(val);
          d.gender = gender;
          d.stats = d.stats.filterBy('gender', gender.id);
          cur.push(d);
        });
        return cur;
      }, []);
    }

    return data.map((d) => {
      d.num_characters = d.stats.reduce((cur, stat) => {
        cur += stat.num_characters;
        return cur;
      }, 0);
      return d;
    });
  }),
  chartData: Ember.computed('data', function() {
    return this.get('data').map((d) => {
      let label = d.race.get('name');
      if (d.clan) {
        label += ' - ' + d.clan.name;
      }
      if (d.gender) {
        label += ' ' + d.gender.symbol;
      }
      return { label: label, value: d.num_characters };
    });
  }),
});
