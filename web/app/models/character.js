import DS from 'ember-data';

export default DS.Model.extend({
  lodestone_id: DS.attr('number'),
  first_name: DS.attr('string'),
  last_name: DS.attr('string'),
  server: DS.belongsTo('server', { async: true }),
});
