# Generated by Django 4.2.7 on 2024-03-26 14:10

from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.contrib.typed_table_block.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0007_auto_20230414_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarytopicpage',
            name='in_depth',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}, template='includes/tableblock.html')), ('typed_table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.blocks.CharBlock()), ('numeric', wagtail.blocks.FloatBlock()), ('rich_text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('note_well', wagtail.blocks.StructBlock([], icon='placeholder', label='Note Well Text')), ('chart', wagtail.blocks.StructBlock([('chart_type', wagtail.blocks.ChoiceBlock(choices=[('line', 'Line Chart'), ('bar', 'Vertical Bar Chart'), ('bar_horizontal', 'Horizontal Bar Chart'), ('area', 'Area Chart'), ('multi', 'Combo Line/Bar/Area Chart'), ('pie', 'Pie Chart'), ('doughnut', 'Doughnut Chart'), ('radar', 'Radar Chart'), ('polar', 'Polar Chart'), ('waterfall', 'Waterfall Chart')], label='Chart Type')), ('title', wagtail.blocks.CharBlock(required=False)), ('datasets', wagtail.blocks.TextBlock(default='{"data":[], "options":{}}')), ('settings', wagtail.blocks.StructBlock([('show_legend', wagtail.blocks.BooleanBlock(default=False, group='General', label='Show legend', required=False)), ('html_legend', wagtail.blocks.BooleanBlock(default=False, group='General', label='Use HTML legend', required=False)), ('legend_position', wagtail.blocks.ChoiceBlock(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], group='General', label='Legend position')), ('reverse_legend', wagtail.blocks.BooleanBlock(default=False, group='General', label='Reverse legend', required=False)), ('show_values_on_chart', wagtail.blocks.BooleanBlock(default=False, group='General', label='Show values on chart', required=False)), ('precision', wagtail.blocks.IntegerBlock(default=1, group='General', label='Precision in labels/tooltips')), ('show_grid', wagtail.blocks.BooleanBlock(default=True, group='General', label='Show Chart Grid', required=False)), ('x_label', wagtail.blocks.CharBlock(group='General', label='X axis label', required=False)), ('stacking', wagtail.blocks.ChoiceBlock(choices=[('none', 'No stacking'), ('stacked', 'Stacked'), ('stacked_100', 'Stacked 100%')], group='General', label='Stacking')), ('unit_override', wagtail.blocks.CharBlock(group='General', label='Unit override', required=False)), ('y_left_min', wagtail.blocks.CharBlock(group='Left_Axis', label='Left Y axis minimum value', required=False)), ('y_left_max', wagtail.blocks.CharBlock(group='Left_Axis', label='Left Y axis maximum value', required=False)), ('y_left_step_size', wagtail.blocks.CharBlock(group='Left_Axis', label='Left Y axis step size', required=False)), ('y_left_label', wagtail.blocks.CharBlock(group='Left_Axis', label='Left Y axis label', required=False)), ('y_left_data_type', wagtail.blocks.ChoiceBlock(choices=[('number', 'Numerical'), ('percentage', 'Percentage')], group='Left_Axis', label='Left Y axis data type', required=False)), ('y_left_precision', wagtail.blocks.IntegerBlock(default=0, group='Left_Axis', label='Left Y axis tick precision')), ('y_left_show', wagtail.blocks.BooleanBlock(default=True, group='Left_Axis', label='Show left axis numbers', required=False)), ('y_right_min', wagtail.blocks.CharBlock(group='Right_Axis', label='Right Y axis minimum value', required=False)), ('y_right_max', wagtail.blocks.CharBlock(group='Right_Axis', label='Right Y axis maximum value', required=False)), ('y_right_step_size', wagtail.blocks.CharBlock(group='Right_Axis', label='Right Y axis step size', required=False)), ('y_right_label', wagtail.blocks.CharBlock(group='Right_Axis', label='Right Y axis label', required=False)), ('y_right_data_type', wagtail.blocks.ChoiceBlock(choices=[('number', 'Numerical'), ('percentage', 'Percentage')], group='Right_Axis', label='Right Y axis data type', required=False)), ('y_right_precision', wagtail.blocks.IntegerBlock(default=0, group='Right_Axis', label='Right Y axis tick precision')), ('y_right_show', wagtail.blocks.BooleanBlock(default=True, group='Right_Axis', label='Show right axis numbers', required=False)), ('pie_border_width', wagtail.blocks.IntegerBlock(default=2, group='Pie_Chart', label='Width of pie slice border')), ('pie_border_color', wagtail.blocks.CharBlock(default='#fff', group='Pie_Chart', label='Color of pie slice border'))])), ('accessible_label', wagtail.blocks.TextBlock(help_text='A description of the chart for screen readers. If not set, a generic description is used, based on the chart title.', required=False))], icon='chart-line'))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='primarytopicpage',
            name='key_info',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}, template='includes/tableblock.html')), ('typed_table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.blocks.CharBlock()), ('numeric', wagtail.blocks.FloatBlock()), ('rich_text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('note_well', wagtail.blocks.StructBlock([], icon='placeholder', label='Note Well Text')), ('chart', wagtail.blocks.StructBlock([('chart_type', wagtail.blocks.ChoiceBlock(choices=[('line', 'Line Chart'), ('bar', 'Vertical Bar Chart'), ('bar_horizontal', 'Horizontal Bar Chart'), ('area', 'Area Chart'), ('multi', 'Combo Line/Bar/Area Chart'), ('pie', 'Pie Chart'), ('doughnut', 'Doughnut Chart'), ('radar', 'Radar Chart'), ('polar', 'Polar Chart'), ('waterfall', 'Waterfall Chart')], label='Chart Type')), ('title', wagtail.blocks.CharBlock(required=False)), ('datasets', wagtail.blocks.TextBlock(default='{"data":[], "options":{}}')), ('settings', wagtail.blocks.StructBlock([('show_legend', wagtail.blocks.BooleanBlock(default=False, group='General', label='Show legend', required=False)), ('html_legend', wagtail.blocks.BooleanBlock(default=False, group='General', label='Use HTML legend', required=False)), ('legend_position', wagtail.blocks.ChoiceBlock(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], group='General', label='Legend position')), ('reverse_legend', wagtail.blocks.BooleanBlock(default=False, group='General', label='Reverse legend', required=False)), ('show_values_on_chart', wagtail.blocks.BooleanBlock(default=False, group='General', label='Show values on chart', required=False)), ('precision', wagtail.blocks.IntegerBlock(default=1, group='General', label='Precision in labels/tooltips')), ('show_grid', wagtail.blocks.BooleanBlock(default=True, group='General', label='Show Chart Grid', required=False)), ('x_label', wagtail.blocks.CharBlock(group='General', label='X axis label', required=False)), ('stacking', wagtail.blocks.ChoiceBlock(choices=[('none', 'No stacking'), ('stacked', 'Stacked'), ('stacked_100', 'Stacked 100%')], group='General', label='Stacking')), ('unit_override', wagtail.blocks.CharBlock(group='General', label='Unit override', required=False)), ('y_left_min', wagtail.blocks.CharBlock(group='Left_Axis', label='Left Y axis minimum value', required=False)), ('y_left_max', wagtail.blocks.CharBlock(group='Left_Axis', label='Left Y axis maximum value', required=False)), ('y_left_step_size', wagtail.blocks.CharBlock(group='Left_Axis', label='Left Y axis step size', required=False)), ('y_left_label', wagtail.blocks.CharBlock(group='Left_Axis', label='Left Y axis label', required=False)), ('y_left_data_type', wagtail.blocks.ChoiceBlock(choices=[('number', 'Numerical'), ('percentage', 'Percentage')], group='Left_Axis', label='Left Y axis data type', required=False)), ('y_left_precision', wagtail.blocks.IntegerBlock(default=0, group='Left_Axis', label='Left Y axis tick precision')), ('y_left_show', wagtail.blocks.BooleanBlock(default=True, group='Left_Axis', label='Show left axis numbers', required=False)), ('y_right_min', wagtail.blocks.CharBlock(group='Right_Axis', label='Right Y axis minimum value', required=False)), ('y_right_max', wagtail.blocks.CharBlock(group='Right_Axis', label='Right Y axis maximum value', required=False)), ('y_right_step_size', wagtail.blocks.CharBlock(group='Right_Axis', label='Right Y axis step size', required=False)), ('y_right_label', wagtail.blocks.CharBlock(group='Right_Axis', label='Right Y axis label', required=False)), ('y_right_data_type', wagtail.blocks.ChoiceBlock(choices=[('number', 'Numerical'), ('percentage', 'Percentage')], group='Right_Axis', label='Right Y axis data type', required=False)), ('y_right_precision', wagtail.blocks.IntegerBlock(default=0, group='Right_Axis', label='Right Y axis tick precision')), ('y_right_show', wagtail.blocks.BooleanBlock(default=True, group='Right_Axis', label='Show right axis numbers', required=False)), ('pie_border_width', wagtail.blocks.IntegerBlock(default=2, group='Pie_Chart', label='Width of pie slice border')), ('pie_border_color', wagtail.blocks.CharBlock(default='#fff', group='Pie_Chart', label='Color of pie slice border'))])), ('accessible_label', wagtail.blocks.TextBlock(help_text='A description of the chart for screen readers. If not set, a generic description is used, based on the chart title.', required=False))], icon='chart-line'))], blank=True, use_json_field=True),
        ),
    ]
